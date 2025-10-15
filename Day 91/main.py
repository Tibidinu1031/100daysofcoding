import requests, json, os


DB_FILE = 'jokes_db.json'


def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_db(db):
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=2)


db = load_db()


while True:
    results = requests.get("https://icanhazdadjoke.com/", headers = {"Accept": "application/json"})
    joke = results.json()
    print()
    print("Check this one out below:\n")
    print(joke['joke'])
    print()
    menu = input("1. Another Joke\n2. Save Joke\n3. View Saved Jokes\n4. Exit\nChoose an option -:> ")

    if menu == '1':
        continue
    elif menu == '2':
        db[joke['id']] = joke['joke']
        save_db(db)
        print("Joke saved!")
    elif menu == '3':
        for items in db.items():
            print(f"ID{items[0]}: {items[1]}")
            print()
    elif menu == '4':
        break
    else:
        print("Invalid option, please try again.")


