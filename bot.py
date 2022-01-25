from aiogram.utils import executor
from create_bot import Dispatcher
from create_bot import dp

import os



async def on_startup(_):
    print('Бот вышел в онлайн')


from handlers import client, admin, other

admin.register_handlers_admin(dp)
client.register_handlers_client(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
