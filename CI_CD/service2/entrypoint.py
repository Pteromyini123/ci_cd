import requests
import sys
import os

SERVICE1_URL = os.getenv("SERVICE1_URL", "http://service1:8080/") 

url = sys.stdin.readline().strip()

#check if input is empty
if not url:
    sys.exit("Error: missing URL on stdin")

#first check status before hashing (if status 4xx/5xx stop the script)
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    message = response.text
except Exception as exc:
    sys.exit(f"Download error: {exc}")

data = ["md5", message]
payload = "\n".join(data) 

try:
    r = requests.post(SERVICE1_URL, data=payload.encode(), timeout=15)
    r.raise_for_status()
except Exception as exc:
    sys.exit(f"service1 error: {exc}")

print(r.text.strip())