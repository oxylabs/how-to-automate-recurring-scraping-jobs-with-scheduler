import requests
import json
from auth_header import get_auth_header

API_URL = "https://data.oxylabs.io/v1/schedules"

payload = json.dumps(
    {
        "cron": "0 16 * * *",
        "items": [
            {
                "source": "amazon_product",
                "query": "B098FKXT8L",
                "parse": True,
            }
        ],
        "end_time": "2032-12-01 16:00:00",
    }
)
headers = {
    "content-type": "application/json",
    "Authorization": get_auth_header("USERNAME", "PASSWORD"),
}

response = requests.post(API_URL, headers=headers, data=payload)

print(response.text)
Í
