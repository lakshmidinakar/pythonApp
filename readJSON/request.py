import requests, json


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
response = requests.get('http://getjson:5000/getJSON')

msg = json.loads(response.content)

print(reverse(msg['message']))
