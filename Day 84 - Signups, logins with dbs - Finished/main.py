import json
import random
import os
import hashlib
from flask import Flask, request, redirect

DB_FILE = "users_db.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=2)

app = Flask(__name__)

@app.route('/')
def index():
    title = "Sign Up/Log In Page"
    page = ""
    f = open("templates/index.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    return page 



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['Email']
        password = request.form['Pass']
    
        db = load_db()

        if username not in db:
            return "Username does not exist. Please sign up first."
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if db[username]['password'] != hashed_password and db[username]['email'] != email and db[username]['username'] != username:
                return "Incorrect password. Please try again."
            else:
                return f"Welcome back, {username}!"

    title = "Log In Page"
    page = ""
    f = open("templates/login.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    return page

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['Pass']
        email = request.form['Email']

        db = load_db()

        if username in db:
            return "Username already exists. Please choose a different username."
        
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
    

