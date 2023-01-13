from loader import dp, bot
from aiogram import types
from states.statess import Fikr
from aiogram.dispatcher import FSMContext
from keyboards.default.back_btn import back
from data.config import ADMINS
from keyboards.inline.answer_btn import answer_to_user


@dp.message_handler(text="📩 Fikr bildirish", state='*')
async def fikr(message: types.Message, state: FSMContext):
    text = "<b>✍️Fikringizni yozib qoldiring!\n\n✅Adminlar uni 24 soat ichida ko'rib chiqadi!\n\n💡Iltimos faqat text xabar yuboring</b>"
    await message.answer(text=text, reply_markup=back)
    await Fikr.izoh.set()


@dp.message_handler(state=Fikr.izoh)
async def izoh(message: types.Message, state: FSMContext):
    msg = message.text
    full_name = message.from_user.full_name
    user_id = message.from_user.get_mention(f"{full_name}", as_html=True)
    text = f"<b>{user_id}</b> botga fikr bildirdi📌\n\n <b>{msg}</b>"

    await message.answer(text="Xabaringiz adminga jo'natildi✔️")
    await bot.send_message(chat_id=ADMINS[0], text=text, reply_markup=answer_to_user)
    await state.finish()