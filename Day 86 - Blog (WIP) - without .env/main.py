import json, random, os, hashlib
from flask import Flask, request, redirect, session
from dotenv import load_dotenv
import datetime


load_dotenv()


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


if 'useroo' not in db:
    db['useroo'] = {
        'password': hashlib.sha256('111'.encode()).hexdigest()}
    save_db(db)


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    title = "Tibi's Blog"
    page = ""
    f = open("templates/index.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    return page


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("pass")

        hashed_pass = hashlib.sha256(password.encode()).hexdigest()

        if username in db and db[username]['password'] == hashed_pass:
            session['useroo'] = username
            return redirect("/add_post")
        else:
            title = "Log In"
            page = ""
            f = open("templates/login.html", "r")
            page = f.read()
            f.close()
            page = page.replace("{title}", title)
            error_msg = "<p style='color:red;'>Invalid credentials</p>"
            page = page.replace("<form", error_msg + "<form")
            return page
        
    title = "Log In"
    page = ""
    f = open("templates/login.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    return page


@app.route("/add_post", methods=["GET","POST"])
def add_post():
    if 'useroo' not in session:
        return redirect("/login")
    
    if request.method == 'POST':
        title = request.form.get("title")
        date = request.form.get("date")
        bodyText = request.form.get("bodytext")

        post = {
            "title": title,
            "date": date,
            "bodyText": bodyText
        }

        if 'posts' not in db:
            db['posts'] = []
        
        db['posts'].append(post)
        save_db(db)

        return redirect("/")
    
    page = ""
    f = open("templates/addPost.html", "r")
    page = f.read()
    f.close()
    return page


@app.route("/logout")
def logout():
    session.pop('useroo', None)
    return redirect("/")


app.run(host="127.0.0.1", port=5000, debug=True)