import requests
import os
from dotenv import load_dotenv

load_dotenv()

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

def generate_image(bio):
    prompt = f"A futuristic portrait of a person who is: {bio}. Style: cinematic, cyberpunk, neon lights."
    url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {REPLICATE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "version": "your-model-version-id",
        "input": {"prompt": prompt}
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        output_url = response.json()['prediction']['output'][0]
        return output_url
    except Exception:
        return "https://via.placeholder.com/512x512.png?text=Book+Cover+Unavailable"