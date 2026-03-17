import time
import requests
import os
import threading

# The URL to ping - default to the provided Render URL if not set in environment
URL = os.environ.get('BACKEND_URL', 'https://notes-5v22.onrender.com/api/health/')

def ping_loop():
    print(f"Starting keep-alive pinger for: {URL}")
    while True:
        try:
            # Setting a timeout to avoid hanging
            response = requests.get(URL, timeout=10)
            print(f"[{time.ctime()}] Health check successful: {response.status_code}")
        except Exception as e:
            print(f"[{time.ctime()}] Health check failed: {e}")
        
        # Sleep for 5 minutes (300 seconds)
        time.sleep(300)

if __name__ == "__main__":
    # Wait a bit for the server to spin up initially
    time.sleep(30)
    ping_loop()
