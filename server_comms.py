import requests
import json

HOST = "127.0.0.1"
PORT = "1337"

username = ""
password = ""

passes = f"http://{HOST}:{PORT}/passwords"
addpass = f"http://{HOST}:{PORT}/add"
rmpass = f"http://{HOST}:{PORT}/remove"

def addPasswordToServer(payload, token, username, password):
    payload["username"] = username
    payload["password"] = password
    payload["token"] = token
    return requests.request("POST", addpass, data=json.dumps(payload)).text

def removePasswordFromServer(payload, token, username):
    payload["username"] = username
    payload["token"] = token
    return requests.request("POST", rmpass, data=json.dumps(payload)).text

def getPasswords(payload, token):
    payload["token"] = token

    return requests.request("POST", passes, data=json.dumps(payload)).text