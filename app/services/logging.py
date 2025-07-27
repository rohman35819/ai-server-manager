import os

LOG_FILE = "data/logs/system.log"

def get_latest_logs(limit=100):
    if not os.path.exists(LOG_FILE):
        return ["Log file not found."]
    
    with open(LOG_FILE, 'r') as file:
        lines = file.readlines()
    
    return lines[-limit:]
