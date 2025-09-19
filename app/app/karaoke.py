from fastapi import APIRouter, UploadFile, File
import librosa, numpy as np

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

def get_pitch_score(user_file, ref_file):
    y_user, sr_user = librosa.load(user_file)
    y_ref, sr_ref = librosa.load(ref_file)

    f0_user, _, _ = librosa.pyin(y_user, fmin=80, fmax=400)
    f0_ref, _, _ = librosa.pyin(y_ref, fmin=80, fmax=400)

    valid = ~np.isnan(f0_user) & ~np.isnan(f0_ref[:len(f0_user)])
    sim = np.mean(np.abs(f0_user[valid]-f0_ref[valid])<30)
    return int(sim*100)
  
