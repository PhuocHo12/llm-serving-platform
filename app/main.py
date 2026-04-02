from fastapi import FastAPI
from api.router import api_router
import uvicorn

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)