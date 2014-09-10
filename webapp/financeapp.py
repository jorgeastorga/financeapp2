#########################
# Imports
#########################
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash


#########################
#
# Config Section
#########################
DATABASE = '/tmp/finance.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'



app = Flask(__name__)
app.config.from_object(__name__)

app.debug = True


#########################
#
# Routes Section
#########################

@app.route('/')
def hello_world():
	return "<h1>Hello World!</h1>"

@app.route('/expenses')
def expenses():
	return render_template("show_expenses.html")

@app.route('/login')
def login():
	return render_template('login.html')

with app.test_request_context():
	print url_for('static', filename='style.css')

if __name__ == '__main__':
	app.run(host='0.0.0.0')