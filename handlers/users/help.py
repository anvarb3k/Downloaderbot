from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from keyboards.inline.dasturchi import admin
from loader import dp


@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message):
    full_name = message.from_user.full_name
    text = f"<b>{full_name} botda qanday muammoga duch keldingiz? Agar qandaydir muammo aniqlagan bo'lsangiz adminga murojaat qiling</b>"
    await message.answer(text=text, reply_markup=admin)
