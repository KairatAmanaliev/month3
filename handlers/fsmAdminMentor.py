from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer('Как зовут?')
        pass
    else:
        await message.answer('Пиши в личке!')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['name'] = message.text
        await FSMAdmin.next()
    await message.answer('Ваше направление?')


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
        await FSMAdmin.next()
    await message.answer('Сколько лет?')



async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
        await FSMAdmin.next()
    await message.answer('Ваша группа?')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f'{data["name"]}' f'{data["direction"]}' f'{data["age"]}' f'{data["group"]}')
        await FSMAdmin.next()
        await message.answer('Все верно?')


async def submit(message: types.Message, state: FSMContext):
    if message.text == 'да':
        await state.finish()
        await message.answer('ты зареган')
    elif message.text == 'заново':
        await FSMAdmin.name.set()
    else:
        await message.answer('Не понял!')


def register_handlers_fsm_context_proxy_storage(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
