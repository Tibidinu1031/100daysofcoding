from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    lang = request.args.get('language', '')
    if lang.lower() == 'patwah':
        return "Wah gwaan mi bredda. Dis a di page weh di greetin dem get turn from English to Patwah. Keep di fyah blaze. One love mi yute. Big up yuhself. Mi kiss. Free Palestine! Bless!"
    return "Hello, if you add ?language=patwah to the URL, you'll see the greeting in Patwah!. Bless!"


app.run(host='127.0.0.1', port=5500, debug=True)