from dotenv import load_dotenv
import os
import requests
import json
import random
from openai import OpenAI
from requests.auth import HTTPBasicAuth


load_dotenv()


# I FUCKING HATE THE NEWS AS A SIDE NOTE BUT THAT's WHAT THIS COURSE DAY IS ABOUT


newsapi = os.getenv("newsapi")
spotifyID = os.getenv('CLIENT_ID')
spotifySecret = os.getenv('CLIENT_SECRET')
country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsapi}"
result = requests.get(url)
data = result.json()
#print(json.dumps(data, indent = 4))


spotifyUrl = "https://accounts.spotify.com/api/token"
spotifyData = {"grant_type": "client_credentials"}
spotifyAuth = HTTPBasicAuth(spotifyID, spotifySecret)
spotifyResponse = requests.post(spotifyUrl, data=spotifyData, auth=spotifyAuth)
spotifyToken = spotifyResponse.json().get("access_token")
spotifyAccessToken = spotifyResponse.json()['access_token']
spotifyYear = random.randint(2000, 2025)
spotifyUrl = 'https://api.spotify.com/v1/search'
spotifyHeaders = {'Authorization': f'Bearer {spotifyAccessToken}'}
spotifySearch = f'?q={spotifyYear}&type=track&limit=5'
spotifyFullLink = f"{spotifyUrl}{spotifySearch}"
spotifyResponse = requests.get(spotifyFullLink, headers = spotifyHeaders)
spotifyData = spotifyResponse.json()



news = []
for articles in data['articles']:
    title = articles['title']
    url = articles['url']
    description = articles['description']
    fullNews = [title, url, description]
    news.append(fullNews)


#for rows in news:
#    for items in rows:
#        print(items)
#        print()
#    print("=====================================================================")
#    print("=====================================================================")
#    print("=====================================================================")
#   print()


client = OpenAI(
    api_key = os.getenv('openaikey'),
    organization = os.getenv('org')
)


print()
print(news[3])
print()
prompt = input("Add prompt: ")
for i, article in enumerate(news):
    placeholder_variants = [f"article {i}", f"news[{i}]"]
    for p in placeholder_variants:
        if p in prompt:
            replacement = f"Title: {article[0]}\nURL: {article[1]}\nDescription: {article[2]}"
            prompt = prompt.replace(p, replacement)


try:
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": prompt}
        ],
        temperature = 0,
        max_tokens = 1000
)
except Exception as e:
    print(f"Error with OpenAI API: {e}")


print()
print(response.choices[0].message.content)
print()


