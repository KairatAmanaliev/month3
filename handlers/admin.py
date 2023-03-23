from aiogram import types, Dispatcher
from config import bot, ADMIN


async def pin(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:
            await message.answer('Не имеешь права')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
            await bot.pin_chat_message(
                message.chat.id,
                message.reply_to_message.from_user.id
                )
        else:
            pass
    else:
        await message.answer('Пиши в группе!')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
