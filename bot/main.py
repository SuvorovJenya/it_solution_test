from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiohttp import ClientSession
import asyncio
import os


TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("get"))
async def fetch_messages(message: Message):
    async with ClientSession() as session:
        async with session.get("http://fastapi-app:8000/api/v1/messages") as resp:
            data = await resp.json()
            if not data:
                await message.answer("Сообщений пока нет.")
            else:
                for msg in data:
                    await message.answer(
                        f"Автор: {msg['author']}\nСообщение: {msg['content']}"
                    )


@dp.message(Command("add"))
async def create_message(message: Message):
    parts = message.text.split(" ", 1)
    if len(parts) < 2:
        await message.answer("Использование: /add <ваше сообщение>")
        return
    content = parts[1]
    async with ClientSession() as session:
        payload = {
            "author": str(message.from_user.username or "Anonymous"),
            "content": content,
        }
        async with session.post(
            "http://fastapi-app:8000/api/v1/message", json=payload
        ) as response:
            if response.status == 200:
                data = await response.json()
                await message.answer(f"Сообщение сохранено: {data['content']}")
            else:
                await message.answer("Ошибка сохранения сообщения.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
