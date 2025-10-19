from dotenv import load_dotenv
import os
import requests
import json
import random
from openai import OpenAI

load_dotenv()

# I FUCKING HATE THE NEWS AS A SIDE NOTE BUT THAT's WHAT THIS COURSE DAY IS ABOUT

newsapi = os.getenv("newsapi")
country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsapi}"
result = requests.get(url)
data = result.json()
#print(json.dumps(data, indent = 4))
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
print(news[1])
print()
prompt = f"Give me more details {news[1]}"

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


