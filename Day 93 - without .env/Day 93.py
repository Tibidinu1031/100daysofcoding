from flask import Flask, request
import os, requests ,json
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)
token = response.json().get("access_token")

accessToken = response.json()['access_token']

#year = 2008
#offset = 0




app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def index():
  page = ""
  f = open('index.html', "r")
  page = f.read()
  f.close()
  if request.method == "POST":
    year = request.form['year']
    url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': f'Bearer {accessToken}'}
    search = f'?q={year}&type=track&limit=5'
    fullLink = f"{url}{search}"
    response = requests.get(fullLink, headers = headers)
    data = response.json()
    for track in data['tracks']['items']:
      page += f"{track['name']} by {track['artists'][0]['name']}"
      page += "<br>"
      if track.get('preview_url'):
        page += f"""
      <audio controls>
        <source src="{track.get('preview_url')}" type="audio/mpeg">
      </audio>
      """
      else:
        directLink = f"{track['external_urls']['spotify']}"
        page += f"""<p>No preview available, but here's the direct link to Spotify below:<br><a href= "{directLink}" target="_blank">{directLink}</a></p>"""
      page += "<hr>"
      page += "<br>"
  return page

app.run(host = "127.0.0.1", port = 5500, debug = True)