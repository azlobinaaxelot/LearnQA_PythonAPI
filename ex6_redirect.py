import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
history = response.history
k = 0
for i in range(len(history)):
    k += 1
    print(history[i].url)

print('Количество редиректов равно', k)

finish_response = response
print(finish_response.url)
