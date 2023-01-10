from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from states.statess import Yuklovchi
from .yuklovchi import tiktok, insta


@dp.message_handler(Text(startswith="https://www.tiktok.com"))
async def tiktoker(message: types.Message):
    msg = message.text
    video = tiktok(msg)
    await message.answer_video(video=video, caption="<b>Video Tiktokdan @fastdownvideobot tomonidan yuklandi✅</b>")


# Instagramdan video yuklashi uchun handler
# ^Reels yuklashu uchun
@dp.message_handler(Text(startswith="https://www.instagram.com/reel/"))
async def tiktoker(message: types.Message):
    msg = message.text
    video = insta(msg)
    await message.answer_video(video=video, caption="<b>Video Instagramdan @fastdownvideobot tomonidan yuklandi✅</b>")

#^Stories yuklashi uchun
@dp.message_handler(Text(startswith="https://www.instagram.com/stories/"))
async def tiktoker(message: types.Message):
    msg = message.text
    video = insta(msg)
    await message.answer_video(video=video, caption="<b>Video Instagramdan @fastdownvideobot tomonidan yuklandi✅</b>")

#^Video yuklashi uchun
@dp.message_handler(Text(startswith="https://www.instagram.com/p/"))
async def tiktoker(message: types.Message):
    msg = message.text
    video = insta(msg)
    await message.answer_video(video=video, caption="<b>Video Instagramdan @fastdownvideobot tomonidan yuklandi✅</b>")
