from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_startup_ideas(topic: str):
    prompt = f"Дай 5 стартап-идей для России по теме '{topic}' с монетизацией."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    text = response.choices[0].message.content

    # защита от None
    if not text:
        return ["Ошибка генерации"]

    return text.split("\n")[:5]
