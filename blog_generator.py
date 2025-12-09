import os
from groq import Groq

def generate_blog(product, keywords):
    print("Generating blog via Groq...")

    # FIX: load Groq after .env is loaded in main.py
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
    Write a 150-200 word SEO blog about "{product['title']}".
    Use these keywords naturally:
    {", ".join(keywords)}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )

    return response.choices[0].message.content
