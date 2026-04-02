import requests
from core.config.vlm import vlm_settings
from openai import OpenAI
class VLMService:
    def __init__(self):
        if vlm_settings.BACKEND == "openai":
            self.client = OpenAI(
                api_key = vlm_settings.OPENAI_API_KEY
            )
        else:
            self.client = OpenAI(
                api_key = "EMPTY",
                base_url = vlm_settings.VLLM_BASE_URL
            )
    def generate(self, image_url, prompt):
        response = self.client.chat.completions.create(
            model = self._get_model(),
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": image_url}}
                    ],
                }
            ],
        )
        return response.choices[0].message.content
    
    def _get_model(self):
        return (
            vlm_settings.OPENAI_MODEL
            if vlm_settings.BACKEND == "openai"
            else vlm_settings.VLLM_MODEL
        )