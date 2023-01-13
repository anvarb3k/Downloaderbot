from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.main import main


@dp.message_handler(text="◀️ Orqaga", state='*')
async def orqaga(message: types.Message, state: FSMContext):
    name = message.from_user.full_name
    await message.answer(f"<b>Assalomu aleykum {name}! Sizni botda ko'rib turganimizdan xursandmiz😊</b>", reply_markup=main)
    await state.finish()