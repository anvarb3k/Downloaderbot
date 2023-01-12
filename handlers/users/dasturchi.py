from loader import dp
from aiogram import types
from states.statess import Yuklovchi
from aiogram.dispatcher import FSMContext
from .yuklovchi import tiktok, insta



@dp.message_handler(text="💻 Dasturchi", state='*')
async def dasturchiman(message: types.Message, state: FSMContext):
    text = "<b>💻 Developer: @uzbsobirov\n\n👤Full name: Sobirov Anvar\n\n🔢Age: 16\n\n🗂Portfolio: @kayzenuz\n\n🗣Instagram: <a href='https://www.instagram.com/'>Touch me</a></b>"
    await message.answer(text=text, disable_web_page_preview=True)
    await state.finish()