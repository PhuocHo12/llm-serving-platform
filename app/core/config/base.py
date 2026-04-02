from pydantic import ConfigDict

class CVSettings(ConfigDict):
    YOLO_MODEL_PATH: str 
    YOLO_CONFIDENCE_THRESHOLD: float

cv_settings = CVSettings()