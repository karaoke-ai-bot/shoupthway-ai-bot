from fastapi import FastAPI, UploadFile, File
import librosa
import numpy as np

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Shoupthway AI Bot is running 🤖🎶"}

@app.post("/analyze-audio/")
async def analyze_audio(file: UploadFile = File(...)):
    try:
        # librosa နဲ့ audio ကိုဖတ်မယ်
        y, sr = librosa.load(file.file, sr=None)
        duration = librosa.get_duration(y=y, sr=sr)
        return {
            "filename": file.filename,
            "duration_seconds": duration,
            "sample_rate": sr
        }
    except Exception as e:
        return {"error": str(e)}
      
