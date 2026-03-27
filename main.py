from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN
from agent import ask_ai
from tools.wallet import address, balance
import threading
from miner import run_mining
from miner import run_mining, auto_mining_loop

AUTO = False
thread = None


async def start(update, ctx):
    await update.message.reply_text("Bot ready")


from miner import run_mining
import threading


async def mine(update, ctx):

    await update.message.reply_text("mining start")

    def job():
        try:
            run_mining()
            print("mining done")
        except Exception as e:
            print(e)

    threading.Thread(target=job).start()

async def claim(update, ctx):

    await update.message.reply_text("claim start")

    def job():
        try:
            run_mining()
        except Exception as e:
            print(e)

    threading.Thread(target=job).start()


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

thread = threading.Thread(
    target=auto_mining_loop,
    daemon=True
)
thread.start()

app.run_polling()
