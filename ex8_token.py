import requests
import json
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = json.loads(response.text)
token = obj['token']
time_task = obj['seconds']
payload = {"token": token}
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
obj = json.loads(response.text)
status = obj['status']
print('Статус', status)
if status == 'Job is NOT ready':
    time.sleep(time_task)
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
    obj = json.loads(response.text)
    status = obj['status']
    result = obj['result']
    print('Статус', status)
    print('Результат', result)
