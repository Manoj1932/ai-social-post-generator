from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# CORS (allow frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("GROQ_API_KEY")

class PostRequest(BaseModel):
    platform: str
    topic: str
    tone: str


@app.post("/generate")
def generate_post(data: PostRequest):

    if not API_KEY:
        return {"error": "GROQ_API_KEY not configured on server"}

    prompt = f"""
You are a social media content creator.

Write a high-engagement social media post.

Platform: {data.platform}
Topic: {data.topic}
Tone: {data.tone}

Rules:
- Use relevant emojis
- Make caption engaging
- Add spacing between sentences
- Include 5 relevant hashtags
- Do NOT explain anything
- Just give the caption
"""

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8
    }

    try:
        response = requests.post(url, headers=headers, json=body, timeout=30)
        result = response.json()

        if "choices" in result:
            content = result["choices"][0]["message"]["content"]
            return {"content": content}

        return {"error": result}

    except Exception as e:
        return {"error": str(e)}