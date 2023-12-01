from flask import Flask, render_template, request, make_response

app = Flask(__name__)

netid = "bml20005"
last_name = "lecza"
ip_address = "172.16.49.16"

@app.route("/")
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('Q1B1', netid)
    resp.set_cookie('Q1B3', ip_address)
    return resp

@app.route("/Q1B2")
def q1b2_index():
    resp = make_response(render_template('q1b2_index.html'))
    resp.set_cookie('Q1B2', last_name)
    return resp