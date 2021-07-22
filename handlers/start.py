from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEK9Ftg-VrajokPtQJZeXDGSRuZlBlkCAACwRgAAoJj_jm2JPo-CmaIgSAE")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nI am 𝙎𝙀𝙀𝙆𝙀𝙍 Bot!
\nMaintained by @SeeKeR_XD 🕉️
\nHit ➤ /help for list of available commands and how they work!
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "User's Manual", url="https://t.me/A_MANUAL_FOR_HUMAN_MECHANISM",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👤 Owner", url="https://t.me/SeeKeR_XD"
                    ),
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/A_MANUAL_FOR_HUMAN_MECHANISM"
                    ),
                    InlineKeyboardButton(
                        "🔊 Updates", url="https://t.me/A_MANUAL_FOR_HUMAN_MECHANISM"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/GroupsVCBot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Updates", url="https://t.me/SeeKeR_XD"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n𝐔𝐒𝐄𝐑 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n𝐀𝐃𝐌𝐈𝐍𝐒 𝐎𝐍𝐋𝐘
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
\n𝘾𝙍𝙀𝘼𝙏𝙀𝘿 𝘽𝙔 𝙎𝙀𝙀𝙆𝙀𝙍🕉️🚩
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐂𝐎𝐍𝐓𝐀𝐂𝐓", url="https://t.me/SeeKeR_XD"
                    )
                ]
            ]
        )
    )
