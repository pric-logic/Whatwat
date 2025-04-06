import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_story(bio):
    prompt = f"""
    Turn the following bio into a sci-fi novel blurb. Make it dramatic, weird, and cinematic. Include a catchy title.

    Bio:
    {bio}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=500
    )

    full_response = response.choices[0].message['content']
    title, *story = full_response.strip().split("\n", 1)
    return title.strip(), story[0].strip() if story else ""