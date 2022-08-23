from flask import Flask, abort

application = Flask(__name__)
app = application

@application.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


