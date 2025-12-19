from fastapi import FastAPI
from auth.router import router as auth_router
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

app.include_router(auth_router)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8140))  # Nomad -> PORT

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        log_level="info",
    )
