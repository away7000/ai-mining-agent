from telegram.ext import Application, MessageHandler, filters
from config import TELEGRAM_TOKEN
from agent import ask_ai


async def handle(update, ctx):

    text = update.message.text

    res = ask_ai(text)

    await update.message.reply_text(res)


app = Application.builder().token(
    TELEGRAM_TOKEN
).build()

app.add_handler(
    MessageHandler(filters.TEXT, handle)
)

app.run_polling()
