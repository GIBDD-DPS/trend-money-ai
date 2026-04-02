import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_startup_ideas(topic: str):
    prompt = f"Найди 5 стартап-идей с российской аудиторией по теме '{topic}' и напиши как зарабатывать деньги."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user", "content": prompt}],
        max_tokens=500
    )
    ideas_text = response.choices[0].message.content
    return ideas_text.split("\n")[:5]