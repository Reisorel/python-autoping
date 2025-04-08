#!/usr/bin/env python3
import requests
from datetime import datetime
import os
import time


# Config
URL = "https://ts-backend-render.onrender.com/api/admin/trees"
LOG_FILE = "ping-script-log.txt"

# Log status with timestamp
def log_status(status: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{now} - {status}\n")
    print(f"{now} - {status}")

# Ping function
def ping():
    try:
        response = requests.get(URL, timeout=10)
        if response.status_code == 200:
            log_status("alive")
            print("Ping succeeded ✅")
        else:
            log_status(f"sleep (HTTP {response.status_code})")
            print(f"Error on server ❌ : {response.status_code}")
    except requests.RequestException as e:
        log_status(f"sleep (Exception: {e})")
        print(f"Network error 😬 : {e}")

# Run the script
if __name__ == "__main__":
    print("Lancement du ping ")
    ping()
