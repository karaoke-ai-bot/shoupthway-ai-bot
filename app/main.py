from fastapi import FastAPI
from app import karaoke, friends

app = FastAPI(title="Shoupthway AI Bot 🤖🎤")

app.include_router(karaoke.router, prefix="/api", tags=["Karaoke"])
app.include_router(friends.router, prefix="/api", tags=["Friends"])

@app.get("/")
def home():
    return {"message": "Welcome to Shoupthway AI Bot 🤖🎶"}
    
