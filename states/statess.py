from aiogram.dispatcher.filters.state import State, StatesGroup

class Yuklovchi(StatesGroup):
    tiktok = State()
    insta = State()
    download = State()