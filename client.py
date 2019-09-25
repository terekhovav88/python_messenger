import requests
import json

response = requests.get('http://127.0.0.1:5000/status')
print(response.json())

response = requests.get('http://127.0.0.1:5000/messages')
print(response.json())

data = {'username': 'Mary', 'text': 'Hi, Jack'}
response = requests.post('http://127.0.0.1:5000/send', json=data)
print(response.json())
