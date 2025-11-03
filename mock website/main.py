from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    logo = "static/assets/Neoteq Logo.png"
    me = "static/assets/Me.jpg"
    page = ""
    f = open("templates/index.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{logo}", logo)
    page = page.replace("{me}", me)
    return page

@app.route('/redirect')
def redirect():
    page = ""
    f = open("templates/redirect.html", "r")
    page = f.read()
    f.close()
    return 

app.run(host='127.0.0.1', port=5500, debug=True)