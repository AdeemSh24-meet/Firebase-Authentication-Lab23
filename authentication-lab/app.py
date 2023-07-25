from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyAFMU0QXS8h71YvyJiTXLLVvKAjgGukgQA",
  "authDomain": "adeem-firebase-authentication.firebaseapp.com",
  "projectId": "adeem-firebase-authentication",
  "storageBucket": "adeem-firebase-authentication.appspot.com",
  "messagingSenderId": "664829280658",
  "appId": "1:664829280658:web:c26ba1069d2b888889014b",
  "databaseURL": "https://adeem-firebase-authentication-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()



app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
            return render_template("signup.html")
    else:
        return render_template("signup.html")


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
    else:
        return render_template("signin.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)