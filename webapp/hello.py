from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) #creates a Flask application object with the __main__ app name

#Setting Flask in debug mode
app.debug = True


############################################################################
# Application routes section
#
#
############################################################################
@app.route('/')
def hello_world():
	return 'Hello World: Are you there testing!'

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

#The actual entry that works for Angular
@app.route('/noproblem')
def noproblem():
	return render_template('sample.html')

@app.route('/redirect')
def redirect_now():
	return redirect('http://www.yahoo.com')

with app.test_request_context():
	print url_for('hello_lucca')
	print url_for('static', filename='style.css')


#If the name of the app is "__main__," then execute the app.run method
#This is the code that starts the execution of the application
if __name__ == '__main__':
	app.run(host='0.0.0.0') #app is the object that represents the Flask application