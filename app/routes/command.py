from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os

router = APIRouter()

# Model untuk request command
class CommandRequest(BaseModel):
    command: str
    api_key: str

@router.post("/", summary="Send a command to AI")
def execute_command(request: CommandRequest):
    # Cek API_KEY
    if request.api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Di sini kamu bisa proses perintah apapun sesuai instruksi
    command = request.command.lower()

    # Contoh respon
    if "hai" in command:
        return {"response": "Halo Bani! Perintah diterima."}
    elif "shutdown" in command:
        # Contoh: jangan benar-benar shutdown komputer kecuali aman
        return {"response": "Shutdown command diterima (simulasi)."}
    else:
        return {"response": f"Perintah '{command}' diterima dan siap diproses."}
