from flask import Flask, request

app = Flask(__name__)

@app.route('/plm', methods = ['POST'])
def plm():
    page = ""
    form = request.form
    if form['username'] == "tibi" or form['username'] == "tibidinu" or form['username'] == "tiberiusdinu":
        page += f"Welcome back, {form['username']}!"
    else:
        page += "Fuck off!"
    return page

@app.route('/')
def home():
    page = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 80 Login Form with Requests</title>
</head>
<body>
    <form method="post" action = "/plm">
    <p>Username: <input type="text" name="username" required></p>
    <p>Email: <input type="email" name="Email" required></p>
    <p>Password: <input type="password" name="Pass" required></p>
    <button type="submit">Login</button>
    </form>
</body>
</html>
    """
    return page

app.run(host = "127.0.0.1", port = 5000, debug = True)