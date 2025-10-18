import requests, json, os
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

artist = input("Artist: ").lower()
artist = artist.replace(" ", "%20")

url = 'https://api.spotify.com/v1/search'
headers = {'Authorization': f'Bearer {accessToken}'}
search = f'?q={artist}&type=track&limit=5'

fullLink = f"{url}{search}"

response = requests.get(fullLink, headers = headers)
data = response.json()


print(json.dumps(data, indent = 4))
#print()
for track in data['tracks']['items']:
    print(f"Track: {track['name']}")
    print(f"Preview URL: {track.get('preview_url')}")
    print("---------------")