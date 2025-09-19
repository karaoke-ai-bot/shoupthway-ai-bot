from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/voice")
async def process_voice(file: UploadFile = File(...)):
    audio = await file.read()
    with open("data/voice.wav", "wb") as f:
        f.write(audio)
    return {"status": "Voice received 🎤"}

@router.post("/duet")
async def duet(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    open("data/voice_userA.wav","wb").write(await file1.read())
    open("data/voice_userB.wav","wb").write(await file2.read())
    return {"status":"Duet received 🎤🎤"}
