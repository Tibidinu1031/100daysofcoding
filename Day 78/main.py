from flask import Flask

list = []

for i in range(78, 101):
    pageNumber = "Page Number"
    loopedList = [pageNumber, i]
    list.append(loopedList)

app = Flask(__name__, static_url_path= '/static')

@app.route('/')
def home():
    title = "Home Reflections"
    pageNumber = "78"
    page = ""
    f = open("template/home.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    page = page.replace("{pageNumber}", pageNumber)
    return page

# This will only work only if you add a / and a page number.
@app.route('/<pageNumber>')
def index(pageNumber):
    if int(pageNumber) == 78:
        title = f"Day {pageNumber} Reflection"
        page = ""
        f = open("template/index.html", "r")
        page = f.read()
        f.close()
        page = page.replace("{pageNumber}", pageNumber)
        page = page.replace("{title}", title)
    else:
        title = f"Day {pageNumber} Reflection"
        page = ""
        f = open("template/index2.html", "r")
        page = f.read()
        f.close()
        page = page.replace("{pageNumber}", pageNumber)
        page = page.replace("{title}", title)
    return page

app.run(host= "127.0.0.1", port= 5000, debug= True)