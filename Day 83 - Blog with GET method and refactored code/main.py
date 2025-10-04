from flask import Flask, redirect, request, render_template
import datetime


app = Flask(__name__, static_url_path="/static")

@app.route("/neoteq")
def neoteq():
  return redirect("https://www.neoteq.us")

@app.route("/green")
def green():
  page = ""
  f = open("templates/green.html", "r")
  page = f.read()
  f.close()
  return page

@app.route("/blue")
def blue():
  page = ""
  f = open("templates/blue.html", "r")
  page = f.read()
  f.close()
  return page

@app.route("/", methods=["GET"])
def index():
  theme = request.args.get("theme", "")
  if theme.lower() == "green":
    return redirect("/green")
  if theme.lower() == "blue":
    return redirect("/blue")
  if theme.lower() == "default":
    return redirect("/")
  now = datetime.datetime.now().date()
  now = str(now)
  page = """
  <html>
  <body>
  <h1>Hello World!</h1>
  <h2>{now}</h2>
  <h3>Here's my first blog entry</h3>
  <h3><a href = "/blog/pageone" target="_blank">Link to blog post 1</a></h3>
  <h3><a href = "/blog/pagetwo">Link to blog post 2</a></h3>
  </body>
  </html>
  """
  page = page.replace("{now}", now)
  return page


@app.route("/pageone")
def pageone():
  number = "1111111111111111111"
  plm = "plm"
  title = "plm1"
  page = ""
  f = open("templates/index.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{number}", number)
  page = page.replace("{plm}", plm)
  page = page.replace("{title}", title)
  return page

@app.route("/blog/pageone")
def blogpageone():
    return redirect("/pageone")


@app.route("/pagetwo")
def pagetwo():
  number = "2222222222222222"
  title = "plm2"
  page = ""
  f = open("templates/index2.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{number}", number)
  page = page.replace("{title}", title)
  return page


@app.route("/blog/pagetwo")
def blogpagetwo():
    return redirect("/pagetwo")


app.run(host = "127.0.0.1", port = 5500, debug = True)