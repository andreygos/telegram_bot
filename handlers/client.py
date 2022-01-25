from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


async def command_start(message: types.Message):
    await message.answer('Добро пожаловать в HotWings!', reply_markup=kb_client)



async def open_locate(message: types.Message):
    await message.answer('input your adress here!')



async def open_wings(message: types.Message):
    await message.answer('Вс-Чт с 11-00 до 22-00, Пт-Сб с 10-00 до 23-00')



#@dp.message_handler(commands=['Меню'])
#async def open_menu(message: types.Message):
#    for ret in cur.execute('SELECT * FROM menu').fetchall():
#        await bot.send_photo(message.text, ret[0], f'{ret[1]}\nОписание: {ret[2]}\Цена {ret[-1]}')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(open_locate, commands=['Расположение'])
    dp.register_message_handler(open_wings, commands=['Режим_работы'])
