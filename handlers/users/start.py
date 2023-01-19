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
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(user_id=user_id,
                    full_name=full_name, username=username)
        await message.answer(f"<b>Assalomu aleykum {full_name}! Sizni botda ko'rib turganimizdan xursandmiz😊</b>", reply_markup=main)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{full_name} bazaga oldin qo'shilgan")
        await message.answer(f"<b>Assalomu aleykum {full_name}! Sizni botda ko'rib turganimizdan xursandmiz😊</b>", reply_markup=main)
