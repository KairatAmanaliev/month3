from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


# @dp.callback_query_handler(text="button_1")


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_1)

    question = "Кто первый полетел в космос?"
    answers = [
        "Юрий Гагарин",
        "Путин",
        "Я",
        "Лепс",
        "Хабиб Нурмагомедов",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        open_period=10,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = "Кто дурак?"
    answers = [
            'я',
            'ты',
            'он',
            'она',
            'они',
        ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="ты",
        open_period=10,
        )


    @dp.message_handler(commands=['mem'])
    async def mem(message: types.Message):
        photo = open('media/1648405122_1-kartinkof-club-p-pozdravlenie-mem-1.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo=photo)


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")
