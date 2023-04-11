import requests
import json
from auth_header import get_auth_header

schedule_id = "1234567890987654321"
API_URL = f"https://data.oxylabs.io/v1/schedules/{schedule_id}/state"

payload = json.dumps({"active": False})
headers = {
    "content-type": "application/json",
    "Authorization": get_auth_header("USERNAME", "PASSWORD"),
}

response = requests.put(API_URL, headers=headers, data=payload)

print(response.text)
