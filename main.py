from aiogram.utils import executor
import logging

from config import dp, bot, ADMIN
from handlers import client, callback, admin, extra, fsmAdminMentor
from database.bot_db import sql_create


async def on_startup(_):
    await bot.send_message(ADMIN[0], 'Я родился!')
    sql_create()

async def on_shutdown(dp):
    await bot.send_message(ADMIN[0], 'Я спать')


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsmAdminMentor.register_handlers_fsm_context_proxy_storage(dp)

extra.register_handlers_client(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
