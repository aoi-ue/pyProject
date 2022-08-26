from flask import Flask  

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1> hello world </h1>"

@app.route("/login")
def log_in():
    return "<h1> log-in </h1>" 
