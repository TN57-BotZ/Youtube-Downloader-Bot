from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support", url="https://t.me/TN57_BotZSupport")],
        [InlineKeyboardButton(
            "Leech & Mirror Zone", url="https://t.me/TN57_Leech")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n I'm Simple Bot To Download YouTube Videos & Thumbnail. 𝙒𝙤𝙧𝙠𝙚𝙙 𝘽𝙮 @TN57_BOTZ"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
