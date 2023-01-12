from loader import dp, bot
from keyboards.inline.subs import check_btn
from aiogram import types
from keyboards.default.main import main
from data.config import CHANNELS
from utils.misc.subscription import check
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="check_obuna")
async def check_sub(call: types.CallbackQuery, state: FSMContext):
    final_status = True
    result = ""

    for channel in CHANNELS:
        status = await check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        invite_link = await channel.export_invite_link()

        if status:
            final_status *= status
            result += f"{channel.title} kanaliga obuna bolgansiz"
        else:
            final_status *= False
            result += f"{channel.title} - {invite_link} /// kanaliga obuna bolmagansiz!!!"

    if final_status:
        await call.message.delete()
        await call.message.answer("Xush kelibsan", reply_markup=main)
    else:
        await call.message.answer(result, disable_web_page_preview=True, reply_markup=check_btn)