from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API KEY (better to use environment variable later)
API_KEY = os.getenv("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")


class PostRequest(BaseModel):
    platform: str
    topic: str
    tone: str


@app.post("/generate")
def generate_post(data: PostRequest):

    prompt = f"""
You are a social media content creator.

Write a high-engagement social media post.

Platform: {data.platform}
Topic: {data.topic}
Tone: {data.tone}

Rules:
- Use relevant emojis in the caption
- Make the caption engaging and friendly
- Add spacing between sentences
- Include 5 relevant hashtags
- Do NOT explain anything
- Just give the post ready to publish
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
        ]
    }

    response = requests.post(url, headers=headers, json=body)
    result = response.json()

    if "choices" in result:
        content = result["choices"][0]["message"]["content"]
        return {"content": content}
    else:
        return {"error": result}