
import requests
import json

url = "http://192.168.1.2:5000/chat"

data = {
    "message": "hi"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)

# Check the status code of the response
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed:", response.json())
