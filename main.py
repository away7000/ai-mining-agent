from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN


async def start(update, ctx):
    await update.message.reply_text("OK start")


async def mine(update, ctx):
    await update.message.reply_text("OK mine")


async def claim(update, ctx):
    await update.message.reply_text("OK claim")


async def auto(update, ctx):
    await update.message.reply_text("OK auto")


async def stop(update, ctx):
    await update.message.reply_text("OK stop")


async def status(update, ctx):
    await update.message.reply_text("OK status")


async def handle(update, ctx):
    await update.message.reply_text("TEXT")


app = Application.builder().token(
    TELEGRAM_TOKEN
).build()


app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("mine", mine))
app.add_handler(CommandHandler("claim", claim))
app.add_handler(CommandHandler("auto", auto))
app.add_handler(CommandHandler("stop", stop))
app.add_handler(CommandHandler("status", status))

app.add_handler(MessageHandler(filters.TEXT, handle))


app.run_polling()
