import requests

post_url = 'http://svc.saltlux.ai:31781'

headers = { 'Content-Type': 'application/json'

}
json_data =  {
    "key": "f2bf109a-d0a2-4931-8fc8-8eaaaf13f6de",
    "serviceId": "01139773605",
    "argument": {
        "question": "아버지가방에들어가셨습니다."
    }
}


response = requests.post(post_url, headers=headers, json = json_data)

print(response.status_code)
print(response.text)
