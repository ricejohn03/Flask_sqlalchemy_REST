#basic Flask app

from flask import Flask
app = Flask(__name__)

@app.rout('/index.html')
def index():
	return'Hello Index'
	
@app.route('/')
def hello_world():
    return 'Hello, World!'
