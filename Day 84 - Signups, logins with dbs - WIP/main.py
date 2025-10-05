import json
import random
import os
import hashlib
from flask import Flask, request, redirect, render_template_string

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
    title = "Log In Page"
    page = ""
    f = open("templates/login.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    return page

@app.route('/signup', methods=['GET','POST'])
def signup():
    title = "Sign Up Page"
    page = ""
    f = open("templates/signup.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    return page


app.run(host='127.0.0.1', port = 5500, debug=True)
    

