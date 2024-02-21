# Python finals
# Password Manager

from cryptography.fernet import Fernet
from dotenv import find_dotenv, load_dotenv
from bottle import *
import json
import os

load_dotenv(find_dotenv())

secret = os.getenv("SECRET")

fernet = Fernet(secret)

def savePasswords(passDict):
    with open('files/passwords.json', 'w+') as confile:
        confile.write(json.dumps(passDict))
        print("Passwords are saved.")

def loadPasswords():
    global passDict
    with open("files/passwords.json", "r+") as confile:
        passDict = json.loads(confile.read())

def checkToken(data):
    userdata = json.loads(data)
    try:
        if "token" in userdata:
            if userdata["token"] == secret:
                return True
        return False
    except ValueError:
        return False

if not os.path.exists("files/passwords.json"):
    with open('files/passwords.json', 'w+') as conf:
        conf.write("{}")

app = Bottle()
passDict = dict()

loadPasswords()

@app.route("/")
def index():
    return "Password manager test :))"

@app.route("/remove", method="POST")
def remove():
    data = request.body.read()
    userdata = dict()
    try:
        userdata = json.loads(data)
    except ValueError:
        return "Invalid Request"
    if checkToken(data):
        try:
            global passDict
            username = userdata["username"]
            passDict.pop(username)
            savePasswords(passDict)
            return f"Removed {username}"
        except KeyError:
            return f"No password stored under {username}"
    return "Prohibited"

@app.route("/add", method="POST")
def add_user():
    data = request.body.read()
    userdata = dict()
    try:
        userdata = json.loads(data)
    except ValueError:
        return "Invalid Request"
    
    if checkToken(data):
        global passDict

        username = userdata["username"]
        password = userdata["password"]
        passDict[username] = password

        savePasswords(passDict)

        return "New password added"
    return "Prohibited"

@app.route("/passwords", method="POST")
def passwords():
    data = request.body.read()
    if checkToken(data):
        return passDict
    return "Prohibited"

run(app, host='127.0.0.1', port=1337, server='gunicorn')


# print(f"Welcome to the password manager :))\nYour passwords are not saved automatically, use {Back.WHITE}{Fore.BLACK}save{Back.RESET}{Fore.RESET} command to save all data.\nUse {Back.WHITE}{Fore.BLACK}help{Back.RESET}{Fore.RESET} command to see all commands available.")

# while True:
#     query = input("> ")
#     match query:
#         case "add":
#             username = input("Enter a username for your account > ")
#             password = input("Enter a password for your account > ")
#             passDict[username] = password

#         case "show":
#             showPasswords(passDict)

#         case "save":
#             savePasswords(passDict)

#         case "erase":
#             username = input("Enter a username > ")
#             try:
#                 passDict.pop(username)
#             except KeyError:
#                 print(f"No password saved under: {username}")

#         case "exit":
#             exit()

#         case _:
#             print("Unknown command.")