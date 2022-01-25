from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()


import os


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)