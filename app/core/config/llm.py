from pydantic import ConfigDict

class LLMSettings(ConfigDict):
    OPEN_API_KEY : str
    MODEL_NAME : str
    TEMPERATURE : float = 0.7

llm_settings = LLMSettings()