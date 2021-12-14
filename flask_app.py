from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/')
def hello():
    return "Welcome Home"


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5001, debug = True)

