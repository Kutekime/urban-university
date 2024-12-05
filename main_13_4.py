import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.types import Message
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

    router = Router()

    @router.message(Command(commands=['start']))
    async def start_message(msg: Message):
        await msg.answer('Привет!\nЯ бот, полезный для твоего здоровья.\nЧтобы начать, напишите слово Calories')

    @router.message(F.text == 'Calories')
    async def calories(msg: Message, state: FSMContext):
        await msg.answer(f'Введите свой возраст, дорогой(ая) {msg.from_user.first_name}!')
        await state.set_state(UserState.age) #await UserState.age.set() -- устаревший метод

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
        #age = (await state.get_data())['age']  # объединил два действия в одно, чтобы избежать создания промежуточной
        # переменной data
        data = await state.get_data()
        bmr = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 4.92 * int(data['age']) + 5 #рассчитал для мужчин
        await msg.answer(f'Ваша норма калорий: {bmr}!')
        #await state.finish() #такого метода теперь нет и насколько я разобрался, ничего подобного вызывать
        # ненужно, хотя есть state.clear(), например


    dp = Dispatcher(storage = MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
