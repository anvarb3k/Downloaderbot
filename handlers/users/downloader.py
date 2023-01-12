from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from states.statess import Yuklovchi
from aiogram.dispatcher import FSMContext
from .yuklovchi import tiktok, insta, stories


@dp.message_handler(text="📥 Video yuklash", state='*')
async def tiktoker(message: types.Message, state: FSMContext):
    text = "<b>📩Menga Instagram va Tiktokdan link yuboring men uni sizga video ko'rinishida yuklab beraman</b>"
    await message.answer(text=text)
    await Yuklovchi.download.set()

@dp.message_handler(Text(startswith="https://www.tiktok.com"), state=Yuklovchi.download)
async def tiktoker(message: types.Message, state: FSMContext):
    msg = message.text
    video = tiktok(link=msg)
    await message.answer_video(video=video, caption="<b>Downloaded by @fastdownvideobot✅</b>")


# Instagramdan video yuklashi uchun handler
# ^Reels yuklashu uchun
@dp.message_handler(Text(startswith="https://www.instagram.com/reel/"), state=Yuklovchi.download)
async def tiktoker(message: types.Message, state: FSMContext):
    msg = message.text
    video = insta(link=msg)
    await message.answer_video(video=video, caption="<b>Downloaded by @fastdownvideobot✅</b>")

#^Stories yuklashi uchun
@dp.message_handler(Text(startswith="https://instagram.com/stories/"), state=Yuklovchi.download)
async def tiktoker(message: types.Message, state: FSMContext):
    msg = message.text
    video = stories(link=msg)
    vido = video['links'][1]['url']
    await message.answer_video(video=vido, caption="<b>Downloaded by @fastdownvideobot✅</b>")

#^Video yuklashi uchun
@dp.message_handler(Text(startswith="https://www.instagram.com/p/"), state=Yuklovchi.download)
async def tiktoker(message: types.Message, state: FSMContext):
    msg = message.text
    video = insta(link=msg)
    await message.answer_video(video=video, caption="<b>Downloaded by @fastdownvideobot✅</b>")
