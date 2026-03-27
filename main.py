import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from agent import ask_ai
from tools.wallet import address, balance
import threading
from miner import run_mining
from miner import run_mining, auto_mining_loop
from skill_parser import parse_skill
from miner_contract import mine, claim_eth, claim_loot
from miner_auto import auto_loop

AUTO = False
thread = None
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

async def start(update, ctx):
    await update.message.reply_text("Bot ready")


from miner import run_mining
import threading


async def mine_cmd(update, ctx):

    await update.message.reply_text("mining...")

    try:
        tx = mine()
        await update.message.reply_text(tx)
    except Exception as e:
        await update.message.reply_text(str(e))

async def claim(update, ctx):

    try:
        tx = claim_eth()
        await update.message.reply_text(tx)
    except Exception as e:
        await update.message.reply_text(str(e))

async def loot(update, ctx):

    tx = claim_loot()

    await update.message.reply_text(tx)
    
async def status(update, ctx):

    try:

        addr = address()
        bal = balance()

    except:
        addr = "?"
        bal = "?"

    try:

        urls = parse_skill()
        total = len(urls)

    except:
        total = 0

    model = os.environ.get("MODEL", "?")
    rpc = os.environ.get("RPC", "?")

    loop_state = "ON" if AUTO else "OFF"

    msg = f"""
=== MINING AGENT STATUS ===

Wallet: {addr}
Balance: {bal}

Loop: {loop_state}
Endpoints: {total}

Model: {model}
RPC: {rpc}

Skill: loaded
"""

    await update.message.reply_text(msg)


async def wallet(update, ctx):
    addr = address()
    bal = balance()
    await update.message.reply_text(f"{addr}\nBalance: {bal}")


async def auto(update, ctx):

    global AUTO

    if AUTO:
        await update.message.reply_text("running")
        return

    AUTO = True

    thread = threading.Thread(
        target=auto_loop,
        daemon=True
    )

    thread.start()

    await update.message.reply_text("AUTO START")

async def stop(update, ctx):

    global AUTO

    AUTO = False

    await update.message.reply_text("STOP")


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
