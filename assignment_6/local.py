import requests
import json
import time

def local_chat(user_msg):
    api_key = "dummy-key"
    url = "http://127.0.0.1:1234/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    req_data = {
        "model": "openai/gpt-oss-20b",
        "messages": [{"role": "user", "content": user_msg}],
    }

    time1 = time.perf_counter()
    response = requests.post(url, data=json.dumps(req_data), headers=headers)
    time2 = time.perf_counter()

    resp = response.json()
    answer = resp["choices"][0]["message"]["content"]
    print(f"Time required: {time2 - time1:.2f} sec")
    return answer
