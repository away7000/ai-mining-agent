from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN
from agent import ask_ai
from loop import auto_loop
import threading
from tools.wallet import address

AUTO = False

async def wallet(update, ctx):

    addr = address()

    await update.message.reply_text(
        f"Wallet:\n{addr}"
    )
    
async def start(update, ctx):
    await update.message.reply_text("Bot ready")


async def mine(update, ctx):

    res = ask_ai("mine")

    await update.message.reply_text(res)


async def claim(update, ctx):

    res = ask_ai("claim")

    await update.message.reply_text(res)


async def status(update, ctx):

    res = ask_ai("status mining")

    await update.message.reply_text(res)


def loop_runner():

    auto_loop()


async def auto(update, ctx):

    global AUTO

    if AUTO:
        await update.message.reply_text("already running")
        return

    AUTO = True

    threading.Thread(
        target=loop_runner,
        daemon=True
    ).start()

    await update.message.reply_text("AUTO MINING START")


async def stop(update, ctx):

    global AUTO

    AUTO = False

    await update.message.reply_text("AUTO STOP")


async def handle(update, ctx):

    text = update.message.text

    res = ask_ai(text)

    await update.message.reply_text(res)


app = Application.builder().token(
    TELEGRAM_TOKEN
).build()


app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("mine", mine))
app.add_handler(CommandHandler("claim", claim))
app.add_handler(CommandHandler("auto", auto))
app.add_handler(CommandHandler("stop", stop))
app.add_handler(CommandHandler("status", status))
app.add_handler(CommandHandler("wallet", wallet))

app.add_handler(MessageHandler(filters.TEXT, handle))


app.run_polling()
