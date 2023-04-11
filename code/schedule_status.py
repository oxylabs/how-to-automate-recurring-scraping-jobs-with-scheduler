import requests
from auth_header import get_auth_header

schedule_id = "1234567890987654321"
url = "https://data.oxylabs.io/v1/schedules/{id}"

headers = {"Authorization": get_auth_header("USERNAME", "PASSWORD")}

response = requests.get(url, headers=headers)

print(response.text)
