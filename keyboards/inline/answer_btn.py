from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

answer_to_user = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️ Javob yozish", callback_data='javobyozish')
        ]
    ]
)