from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    page = ""
    f = open("templates/ruarobot.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", "Are You a Robot?")
    return page

@app.route("/ruarobot", methods = ['POST'])
def ruarobot():
    page = ""
    form = request.form
    if form['metal'].lower() == "yes" or form["infinity"].lower() != "infinity" or form["menu"].lower() != "human food":
        page += "You're a robot!"
    else:
        page += "You're not a robot!"
    return page

app.run(host = "127.0.0.1", port = 5000, debug=True)