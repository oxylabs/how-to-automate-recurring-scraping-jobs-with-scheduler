import requests
import json

from auth_header import get_auth_header


def deactivate(schedule_id):
    url = f"https://data.oxylabs.io/v1/schedules/{schedule_id}/state"

    payload = json.dumps({"active": False})
    headers = {
        "content-type": "application/json",
        "Authorization": get_auth_header("USERNAME", "PASSWORD"),
    }

    response = requests.put(url, headers=headers, data=payload)

    print(response.text)


def get_all_schedules():
    url = "https://data.oxylabs.io/v1/schedules"
    headers = {"Authorization": get_auth_header("USERNAME", "PASSWORD")}

    response = requests.get(url, headers=headers)
    return response.json().get("schedules")


if __name__ == "__main__":
    schedules = get_all_schedules()
    for schedule in schedules:
        deactivate(schedule)
