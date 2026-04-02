from pydantic import ConfigDict
from typing import Literal

class VLMSettings(ConfigDict):
    # chọn backend
    BACKEND: Literal["openai", "vllm"] = "openai"

    # =========== OpenAI ===========
    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL: str = "gpt-4o-mini"

    # =========== vLLM ===========
    VLLM_BASE_URL: str = "http://localhost:8001"
    VLLM_MODEL: str = "mistralai/Mistral-7B-Instruct"
    VLLM_TEMPERATURE: float = 0.7

    # common
    TIMEOUT: int = 30

    class Config:
        env_prefix = "VLM_"
        env_file = ".env"

vlm_settings = VLMSettings()