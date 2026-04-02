from dotenv import load_dotenv
load_dotenv()
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from openai_api import generate_startup_ideas
from robokassa import create_payment_link

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def ideas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args) if context.args else "AI tools"
    ideas_list = generate_startup_ideas(text)
    msg = "\n\n".join([f"{i+1}. {idea}" for i, idea in enumerate(ideas_list)])
    payment_link = create_payment_link(update.effective_user.id)
    await update.message.reply_text(f"{msg}\n\nДля полного доступа к 20+ идеям в день: {payment_link}")

def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("ideas", ideas))
    print("Bot started...")
    app.run_polling()