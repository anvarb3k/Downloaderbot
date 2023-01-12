from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📥 Video yuklash"), KeyboardButton(text="💻 Dasturchi")]
    ],
    resize_keyboard=True, one_time_keyboard=True
)