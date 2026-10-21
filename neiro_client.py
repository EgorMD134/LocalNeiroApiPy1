import requests
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

url = "http://localhost:1234/v1/chat/completions"

headers = {
    "Content-Type": "application/json"
}

def get_ansver_from_neiro(promt):
    payload = {
        "model": "gemma-3-1b-it",          
        "messages": [
            {"role": "user", "content": promt}
        ],
        "temperature": 0.7
    }

    response = requests.post(url,headers=headers,data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else :
        return response.status_code

print(get_ansver_from_neiro("кто ты?"))