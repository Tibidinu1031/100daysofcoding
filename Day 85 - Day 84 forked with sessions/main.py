import json
import random
import os
import hashlib
from flask import Flask, request, redirect, session
from dotenv import load_dotenv

DB_FILE = "users_db.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=2)

db = load_db()
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route('/')
def index():
    title = "Sign Up/Log In Page"
    page = ""
    f = open("templates/index.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    return page 


@app.route('/welcome')
def welcome():
    page = f"""
    <h1>Welcome!</h1>
    <button type="button" onclick="window.location.href='/logout'">Logout</button>
    """
    return page


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')



@app.route('/login', methods=['GET','POST'])
def login():
    if session.get('loggedIn'):
        return redirect('/welcome')
    if request.method == "POST":
        username = request.form['username']
        password = request.form['Pass']
        email = request.form['Email']

        db = load_db()

        if username not in db:
            return "Username does not exist. Please sign up first."
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if db[username]['password'] != hashed_password or db[username]['email'] != email or db[username]['username'] != username:
            return "Incorrect credentials. Please try again."
        else:
            session['loggedIn'] = request.form['username']
            return redirect('/welcome')

    title = "Log In Page"
    page = ""
    f = open("templates/login.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    return page


@app.route('/signup', methods=['GET','POST'])
def signup():
    if session.get('loggedIn'):
        return redirect('/welcome')
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['Email']
        password = request.form['Pass']

        db = load_db()

        if username in db:
            return "Username already exists. Please choose a different one."
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        db[username] = {
            'username': username,
            'email': email,
            'password': hashed_password
        }

        save_db(db)

        return redirect('/login')

    title = "Sign Up Page"
    page = ""
    f = open("templates/signup.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    return page


app.run(host='127.0.0.1', port = 5500, debug=True)
    

