async def ideas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("IDEAS COMMAND RECEIVED")  # 👈 добавь

    try:
        text = " ".join(context.args) if context.args else "AI tools"

        print("USER INPUT:", text)  # 👈 добавь

        ideas_list = generate_startup_ideas(text)

        print("IDEAS:", ideas_list)  # 👈 добавь

        msg = "\n\n".join([f"{i+1}. {idea}" for i, idea in enumerate(ideas_list)])

        payment_link = create_payment_link(update.effective_user.id)

        await update.message.reply_text(
            f"{msg}\n\n💰 Полный доступ:\n{payment_link}"
        )

    except Exception as e:
        print("ERROR:", e)  # 👈 самое важное
        await update.message.reply_text("Ошибка при генерации 😢")
