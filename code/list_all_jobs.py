import requests
from auth_header import get_auth_header

url = "https://data.oxylabs.io/v1/schedules"


headers = {"Authorization": get_auth_header("USERNAME", "PASSWORD")}

response = requests.get(url, headers=headers)

print(response.text)
