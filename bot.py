import os, logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("betgrap")

BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLOWED_IDS = {int(x.strip()) for x in os.getenv("ALLOWED_IDS","").split(",") if x.strip().isdigit()}

def authorized(user_id: int) -> bool:
    return (not ALLOWED_IDS) or (user_id in ALLOWED_IDS)

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if not authorized(uid):
        await update.message.reply_text("Yetkin yok.")
        return
    await update.message.reply_text("✅ BetGrapBot aktif!")

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN yok.")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    main()
