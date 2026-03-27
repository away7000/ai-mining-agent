from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN
from agent import ask_ai
from miner import auto_mining_loop
from tools.wallet import address, balance
import threading

AUTO = False
thread = None


async def start(update, ctx):
    await update.message.reply_text("Bot ready")


async def mine(update, ctx):

    await update.message.reply_text("mining start")

    try:
        run_mining()
        await update.message.reply_text("mining done")
    except Exception as e:
        await update.message.reply_text(str(e))


async def claim(update, ctx):

    await update.message.reply_text("claim start")

    try:
        run_mining()
        await update.message.reply_text("claim done")
    except Exception as e:
        await update.message.reply_text(str(e))


async def status(update, ctx):
    res = ask_ai("status")
    await update.message.reply_text(str(res))


async def wallet(update, ctx):
    addr = address()
    bal = balance()
    await update.message.reply_text(f"{addr}\nBalance: {bal}")


async def auto(update, ctx):
    global AUTO, thread

    if AUTO:
        await update.message.reply_text("already running")
        return

    AUTO = True

    thread = threading.Thread(
        target=auto_mining_loop,
        daemon=True
    )

    thread.start()

    await update.message.reply_text("AUTO START")


async def stop(update, ctx):
    global AUTO
    AUTO = False
    await update.message.reply_text("AUTO STOP")


async def handle(update, ctx):
    text = update.message.text
    res = ask_ai(text)
    await update.message.reply_text(str(res))


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


print("BOT RUNNING")

app.run_polling()
