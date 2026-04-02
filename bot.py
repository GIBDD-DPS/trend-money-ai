import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

print("TOKEN:", TELEGRAM_TOKEN)  # 👈 ВОТ ЗДЕСЬ, после объявления

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
...
