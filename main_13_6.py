import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.types import (Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup ,
                           InlineKeyboardButton)
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class UserState(StatesGroup):
    age, growth, weight = State(), State(), State()

async def main():
    api = 'АПИ ВАШЕГО БОТА'
    bot = Bot(token = api, default = DefaultBotProperties(parse_mode=ParseMode.HTML))


    btn1 = KeyboardButton(text = 'Рассчитать')
    btn2 = KeyboardButton(text = 'Информация')
    kb_list = [[btn1, btn2]]
    kb = ReplyKeyboardMarkup(keyboard = kb_list, resize_keyboard = True)


    inline_btn1 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calculate')
    inline_btn2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    ikb_list = [[inline_btn1, inline_btn2]]
    inline_kb = InlineKeyboardMarkup(inline_keyboard = ikb_list)

    router = Router()

    @router.message(Command(commands=['start']))
    async def start_message(msg: Message):
        await msg.answer('Нажмите на пункт меню ниже:', reply_markup = kb)

    @router.message(F.text == 'Информация')
    async def info(msg: Message):
        await msg.answer('Привет!\nЯ бот, полезный для твоего здоровья.\nЧтобы начать, нажмите кнопку "Рассчитать"')

    @router.message(F.text == 'Рассчитать')
    async def main_menu(msg: Message):
        await msg.answer('А вот встроенное (inline) меню прямо в чат:', reply_markup=inline_kb)

    @router.callback_query(F.data == 'calculate')
    async def calories(call: CallbackQuery, state: FSMContext):
        await call.message.answer(f'Введите свой возраст, дорогой(ая) {call.from_user.first_name}!')
        await state.set_state(UserState.age)
        await call.answer()

    @router.callback_query(F.data == 'formulas')
    async  def get_formulas(call: CallbackQuery):
        await call.message.answer('Для мужчин:\n'
                         'BMR = 10 × вес (кг) + 6,25 × рост (см) – 5 × возраст (лет) + 5\n\n'
                         'Для женщин:\n'
                         'BMR = 10 × вес (кг) + 6,25 × рост (см) – 5 × возраст (лет) – 161')
        await call.answer()

    @router.message(UserState.age)
    async def set_age(msg: Message, state: FSMContext):
        await state.update_data(age = msg.text)
        await msg.answer('Введите свой рост!')
        await state.set_state(UserState.growth)

    @router.message(UserState.growth)
    async def set_growth(msg: Message, state: FSMContext):
        await state.update_data(growth = msg.text)
        await msg.answer('Введите свой вес!')
        await state.set_state(UserState.weight)

    @router.message(UserState.weight)
    async def set_weight_and_show_calories(msg: Message, state: FSMContext):
        await state.update_data(weight = msg.text)
        data = await state.get_data()
        bmr = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 4.92 * int(data['age']) + 5 #рассчитал для мужчин
        await msg.answer(f'Ваша норма калорий: {bmr}!')
        #await state.finish() #такого метода теперь нет и насколько я разобрался, ничего подобного вызывать
        # ненужно, хотя есть state.clear(), например


    dp = Dispatcher(storage = MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot, allowed_updates = dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
