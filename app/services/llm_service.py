import requests

from core.config import VLLM_URL

def chat_with_vllm(messages):
    url = f"{VLLM_URL}/chat/completions"

    payload = {
        "model": "mistralai/Mistral-7B-Intruct",
        "messages": [m.dict() for m in messages],
        "temperature": 0.7
    }

    response = requests.post(url,json = payload)
    data = response.json()

    return data["choice"][0]["message"]["content"]