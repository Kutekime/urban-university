import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage


async def main():
    api = 'АПИ ВАШЕГО БОТА'
    bot = Bot(token = api, default = DefaultBotProperties(parse_mode=ParseMode.HTML)) #parse_mode=ParseMode.HTML - уже устарело

    router = Router()

    #и ещё устарела такая запись @router.message(Command("start")).. обновил. Теперь через именованный аргумент
    @router.message(F.text.in_({'Cuteman', 'ff'})) #F.text == 'word' для простого фильтра
    async def cuteman_message(msg: Message):
        await msg.answer(f'Вы написали кодовое слово, дорогой(ая) {msg.from_user.first_name}!')

    @router.message(Command(commands = ['start']))
    async def start_message(msg: Message):
        await msg.answer('Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение')

    @router.message()
    async def all_message(msg: Message):
        #print(f'Мы получили сообщение!\nВот оно: {msg.text}\nВведите команду /start, чтобы начать общение!')
        await msg.answer(f'Твой ID: {msg.from_user.id}')


    dp = Dispatcher(storage = MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    #logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
