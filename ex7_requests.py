import requests

#1
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

#2
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

#3
method = input("Укажите метод, с помощью которого вы делаете запрос ")
params = {"method": method}

if method == 'GET':
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
    print(response.text)

if method == 'POST':
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print(response.text)

if method == 'PUT':
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print(response.text)

if method == 'DELETE':
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print(response.text)

#4
def output_params(method, param, response):
    print('Метод ', method)
    print('Параметр ', param)
    print('Статус код ', response.status_code)
    print('Текст ответа ', response.text)
    print('---------------------------------------')


s_m = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH"]
for method in s_m:
    if method == "GET":
        for param in s_m:
            params = {"method": param}
            response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=params)
            output_params(method, param, response)
    elif method == "POST":
        for param in s_m:
            data = {"method": param}
            response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=data)
            output_params(method, param, response)
    elif method == "PUT":
        for param in s_m:
            data = {"method": param}
            response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=data)
            output_params(method, param, response)
    elif method == "DELETE":
        for param in s_m:
            data = {"method": param}
            response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=data)
            output_params(method, param, response)
    elif method == "PATCH":
        for param in s_m:
            data = {"method": param}
            response = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type", data=data)
            output_params(method, param, response)
    elif method == "HEAD":
        for param in s_m:
            data = {"method": param}
            response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=data)
            output_params(method, param, response)
    elif method == "OPTIONS":
        for param in s_m:
            data = {"method": param}
            response = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type", data=data)
            output_params(method, param, response)