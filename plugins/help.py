from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Just Send YouTube Link And Select Desired Format. Then I am send The Content As Video Or File ☺️. Don't Send Live YouTube Link🙅. Any Error contact @TN57_BotZSupport"
    await message.reply_text(helptxt)
