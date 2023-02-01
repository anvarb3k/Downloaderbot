from loader import dp, bot
from aiogram import types
from states.statess import Fikr
from aiogram.dispatcher import FSMContext
from keyboards.default.back_btn import back
from data.config import ADMINS
from keyboards.inline.answer_btn import answer_to_user

# Foydananuvchi fikrini bildirishi uchun
@dp.message_handler(text="📩 Fikr bildirish", state='*')
async def fikr(message: types.Message, state: FSMContext):
    text = "<b>✍️Fikringizni yozib qoldiring!\n\n✅Adminlar uni 24 soat ichida ko'rib chiqadi!\n\n💡Iltimos faqat text xabar yuboring</b>"
    await message.answer(text=text, reply_markup=back)
    await Fikr.izoh.set()

# Foydalanuvchi fikrini ilib olamiz `state` orqali
@dp.message_handler(state=Fikr.izoh)
async def izoh(message: types.Message, state: FSMContext):
    msg = message.text
    full_name = message.from_user.full_name
    userid = message.from_user.id
    await state.update_data(
        {'userid': userid}
    )
    user_id = message.from_user.get_mention(f"{full_name}", as_html=True)
    text = f"<b>{user_id}</b> botga fikr bildirdi📌[{userid}]\n\n <b>{msg}</b>"

    await message.answer(text="Xabaringiz adminga jo'natildi✔️")
    await bot.send_message(chat_id=ADMINS[0], text=text, reply_markup=answer_to_user)
    await state.finish()


# Fikrini bildirgan foydalanuvchiga javob yozamiz
@dp.callback_query_handler(text="javobyozish", state='*', user_id=ADMINS[0])
async def javobyozish(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text="Kimga javob yozmoqchisiz? Id  va matn kiriting👇👇👇\n\nExp: Foydalanuvchi idsi, Javob matni")
    await Fikr.answer.set()


# Adminning javobini foydalanuvchiga yuborish uchun
@dp.message_handler(state=Fikr.answer)
async def answer(message: types.Message, state: FSMContext):
    msg = message.text
    # xabarni verguldan keyin bo'lib olamiz `id` va `javob` ni olish uchun
    response = msg.split(',')
    # Agar admin xabari uzunligi 2 ga teng bo'lsa foydalanuvchiga yuboradi
    if len(response) == 2:
        user_id = response[0]
        javob = response[1]
        text = f"<b>Admindan sizga javob keldi👇\n\n--{javob}</b>"
        await bot.send_message(chat_id=user_id, text=text)
        await bot.send_message(chat_id=ADMINS[0], text="<b>Javobingiz yuborildi✅</b>")
        await state.finish()
    # Agar xabar 2dan katta bo'lsa yani => 121, 231, sddsd
    elif len(response) > 2:
        await bot.send_message(chat_id=ADMINS[0], text="<b>Siz javobni xato shaklda kiritdingiz!!! Boshqattan kiriting👇\n\nExp: Foydalanuvchi idsi, Javob matni</b>")
        await Fikr.answer.set()
    # Aks xolda => 212121 or sdsdsd
    else:
        await bot.send_message(chat_id=ADMINS[0], text="<b>Siz javobni xato shaklda kiritdingiz!!! Boshqattan kiriting👇\n\nExp: Foydalanuvchi idsi, Javob matni</b>")
        await Fikr.answer.set()
