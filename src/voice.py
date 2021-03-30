import requests

#post_url = 'http://svc.saltlux.ai:31781'

headers = { 'Content-Type': 'application/json'

}


json_data = {
    "key": "f2bf109a-d0a2-4931-8fc8-8eaaaf13f6de",
    "serviceId": "01514175946",
    "argument": {
        "voice": "gangwon",
        "text": "지는 치킨을 먹어유. 지는 벤틀리고유. 아빠 , 형 어딨는지 모르니 찾지 마세유.",
        "cache": "Ture",
        "replace": "Ture",
        "type": "wav"
    }
}


response = requests.post(headers=headers, json = json_data)

#print(response.status_code)

