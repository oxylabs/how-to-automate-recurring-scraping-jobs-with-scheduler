import requests
import json
from auth_header import get_auth_header

API_URL = "https://data.oxylabs.io/v1/schedules"

payload = json.dumps(
    {
        "cron": "0 16 * * *",
        "items": [
            {
                "source": "amazon",
                "url": "https://www.amazon.com/dp/B098FKXT8L",
                "callback_url": "https://callback.url",
                "storage_type": "s3",
                "storage_url": "s3://yourown.s3.bucket/path",
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
