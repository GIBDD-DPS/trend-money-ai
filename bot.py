import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Получаем токен
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

print("TOKEN:", TELEGRAM_TOKEN)  # для отладки (потом можно убрать)

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from openai_api import generate_startup_ideas
from robokassa import create_payment_link


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Бот работает!\n\nНапиши:\n/ideas AI tools"
    )


# Команда /ideas
async def ideas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = " ".join(context.args) if context.args else "AI tools"

        ideas_list = generate_startup_ideas(text)

        msg = "\n\n".join([f"{i+1}. {idea}" for i, idea in enumerate(ideas_list)])

        payment_link = create_payment_link(update.effective_user.id)

        await update.message.reply_text(
            f"{msg}\n\n💰 Полный доступ (20+ идей):\n{payment_link}"
        )

    except Exception as e:
        print("ERROR:", e)
        await update.message.reply_text("Ошибка при генерации 😢")


# Запуск бота
def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ideas", ideas))

    print("Bot started...")
    app.run_polling()
