from flask import Flask

app = Flask(__name__)
#@app.route('/')

#@app.route('/')
#def hello_world():
    #return 'Hello world'

@app.route('/')
def counting():
    return '1 2 3 4 5'
    