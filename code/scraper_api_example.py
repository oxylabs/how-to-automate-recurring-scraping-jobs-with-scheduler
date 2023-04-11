import requests

payload = {
    "source": "amazon_product",  # returns product information
    "query": "B098FKXT8L",
    "parse": True,
}


response = requests.post(
    "https://realtime.oxylabs.io/v1/queries",
    auth=("USERNAME", "PASSWORD"),
    json=payload,
)


print(response.json())
