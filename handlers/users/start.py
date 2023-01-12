import sqlite3
from data.config import CHANNELS
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main import main
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.inline.subs import check_btn
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    channels_format = ""
    markup = InlineKeyboardMarkup(row_width=1)
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        channels_format += f"<a href='{invite_link}'>{chat.title}</a>"
        markup.insert(InlineKeyboardButton(text=chat.title, url=invite_link))
    markup.insert(InlineKeyboardButton(text="Obunani tekshirish", callback_data='check_obuna'))
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"Quyidagi kanallarga obuna bo'ling!", reply_markup=markup, disable_web_page_preview=True)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"Quyidagi kanallarga obuna bo'ling!", reply_markup=markup, disable_web_page_preview=True)
