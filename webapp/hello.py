from flask import Flask, url_for, render_template, redirect
app = Flask(__name__)

#Setting Flask in debug mode
app.debug = True

@app.route('/')
def hello_world():
	return 'Hello World: Are you there Jorge!'

@app.route('/jorge/')
def hello_jorge():
	return "<h1>Jorge H1</h1>" + "<h2>Jorge H2</h2>"

@app.route('/lucca')
def hello_lucca():
	return "<h1>Hello Lucca! Just having fun with some toys!</h1>"

@app.route('/login/<username>')
def print_username(username):
	return 'User %s' % username

@app.route('/user/<id>')
def print_userid(id):
	return 'User ID: %s' % id

@app.route('/render_test')
def render_test():
	return render_template('show_entries.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/noproblem')
def noproblem():
	return render_template('sample.html')

@app.route('/redirect')
def redirect_now():
	return redirect('http://www.yahoo.com')

with app.test_request_context():
	print url_for('hello_lucca')
	print url_for('static', filename='style.css')


if __name__ == '__main__':
	app.run(host='0.0.0.0')