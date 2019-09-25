import flask
import time
import json
import requests
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

messages = [
    {'username': "Jack", 'time': time.time(), 'text': "Hello!"},
    {'username': "Mary", 'time': time.time(), 'text': "Hi Jack!"}
]

users = {
    #username: password
    "Jack": "Black",
    "Marie": "123456"
}

@app.route("/")
def hello_view():
    return "Hello World !"

@app.route("/status")
def status_view():
    return {
        'status': True,
        'time': datetime.now().strftime('%Y-%m-%d %M:%S')
    }

@app.route("/messages")
def messages_view():
    return {'messages': messages}

@app.route("/send", methods=['POST'])
def send_view():
    """
    Оправить сообщения всем.
    input:{"username":str, "password":str "text":str}
    :return: {"ok": bool}
    """
    print(request.json)
    username = request.json["username"]
    password = request.json["password"]
    text = request.json["text"]

    if username not in users and users[username] != password:
        return {'ok': False}

    messages.append({'username': username, 'time': time.time(), 'text': text})
    return {'ok': True}

if __name__ == '__main__':
    app.run()