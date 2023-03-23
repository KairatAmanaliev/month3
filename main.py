from aiogram.utils import executor
import logging

from config import dp
from handlers import client, callback, admin, extra, fsmAdminMentor

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsmAdminMentor.register_handlers_fsm_context_proxy_storage(dp)

extra.register_handlers_client(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
