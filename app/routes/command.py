from fastapi import APIRouter, Header, HTTPException
from app.services.executor import execute_command

router = APIRouter()

@router.post("/")
def run_command(command: str, x_api_key: str = Header(...)):
    from os import getenv
    if x_api_key != getenv("API_KEY_OWNER"):
        raise HTTPException(status_code=403, detail="Forbidden")
    result = execute_command(command)
    return {"status": "ok", "command": command, "result": result}
