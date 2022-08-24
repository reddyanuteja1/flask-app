from flask import Flask, abort

application = Flask(__name__)

@application.route('/',methods=['GET','POST'])
def hello_world():
    return '<h1>Hello, World!</h1>'


