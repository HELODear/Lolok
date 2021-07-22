from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"**Join ➤ [Awesome Blossoms 🌸](https://t.me/hindi_chatting_india)**\n\n**CONTACT HERE ➤ [𝐕𝐀𝐒𝐔](https://t.me/xxvasu)**")
  return                        
