from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    page = ""
    f = open("templates/index.html", "r")
    page = f.read()
    f.close()
    return page

@app.route("/ruarobot", methods = ['GET','POST'])
def ruarobot():
    page = ""
    f = open("templates/ruarobot.html", "r")
    page = f.read()
    f.close()
    if request.method == 'POST':
        metal = request.form.get('metal')
        infinity = request.form.get('infinity')
        menu = request.form.get('menu')

        if metal and infinity and menu:
            if metal == "yes" and infinity != 'infinity' and menu != "Human Food":
                page += "<p>Beep Boop! I am a robot!</p>"
            else:
                page += "<p>I am not a robot!</p>"
        else:
            page += "<p>Error: form incomplete!</p>"
    return page

app.run(host = "127.0.0.1", port = 5000, debug=True)