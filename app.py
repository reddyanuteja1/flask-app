from markupsafe import escape
from flask import Flask, abort

application = Flask(__name__)
app = application

@application.route('/')
@application.route('/index/')
def hello():
    return '<h1>Hello, World!</h1>'


@application.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@application.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@application.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)

@application.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)

