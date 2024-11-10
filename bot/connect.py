import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from aiogram.client.bot import DefaultBotProperties

load_dotenv()

bot = Bot(token=os.getenv("API_TOKEN_TELEGRAM"), default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher(storage=MemoryStorage())