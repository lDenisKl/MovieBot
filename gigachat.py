import requests
import uuid
import json
import time

class GigaChat:
    urlOAuth = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    urlCompletions = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    scope = 'scope=GIGACHAT_API_PERS'
    model = 'GigaChat'

    gcAutorization = ''
    gcToken = ''
    gcTokenExpiresAt = 0

    def __init__(self, secret):
        self.gcAutorization = secret.gcAutorization

    def updateGCToken(self):
        if self.gcTokenExpiresAt - time.time() < 1000:
            return self.getGCToken()
        return True

    def getGCToken(self):
        UUID = uuid.uuid4()
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': str(UUID),
            'Authorization': 'Basic ' + self.gcAutorization
        }

        response = requests.request("POST", self.urlOAuth, headers=headers, data=self.scope, verify='chain.pem')
        resp = response.json()
        if resp.get('access_token'):
            self.gcToken = resp.get('access_token')
            self.gcTokenExpiresAt = resp.get('expires_at')
            return True
        return False

    def ask(self, question):
        if not self.updateGCToken():
            return False

        # print(question)
        question = 'Выбери фильм похожий по жанру и сюжету на "' + question + '".'
        data = json.dumps({
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": "Ты кино-эксперт. Предложи один фильм. Выведи ответ в виде:"
                               "✅Название: *,\n"
                               "🕐Год выпуска: *,\n"
                               "🔞Возрастное ограничение: *,\n"
                               "📈Рейтинг: *,\n"
                               "💬Описание: *.\n"
                               "Вставь данные вместо *. Вместо '\n' поставь enter"
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            "temperature": 1,
            "top_p": 0.1,
            "n": 1,
            "stream": False,
            "max_tokens": 400,
            "repetition_penalty": 1
        })

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.gcToken}'
        }

        response = requests.request("POST", self.urlCompletions, headers=headers, data=data, verify='chain.pem')
        # print(response.text)
        resp = response.json()
        if 'choices' in resp:
            return str(resp['choices'][0]['message']['content'])
        
        return False
