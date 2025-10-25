from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import json
import random
from openai import OpenAI
from requests.auth import HTTPBasicAuth

load_dotenv()

email = os.getenv('email')

url = "https://en.wikipedia.org/wiki/The_Buddha"

# Add headers with a User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
article = soup.find_all("div", {"class": "mw-page-container"})

for section in article:
    content = section.find_all("p")
    for paragraph in content:
        text = paragraph.get_text()
        if text.strip():
            print(text)
            print()

client = OpenAI(
    api_key = os.getenv('openaikey'),
    organization = os.getenv('org')
)


print()
print()
content = soup.find('div', {'id': 'mw-content-text'})
paragraphs = content.find_all('p') if content else []
article_text = '\n\n'.join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

print("Article scraped successfully!")
print(f"Article length: {len(article_text)} characters\n")


client = OpenAI(
    api_key=os.getenv('openaikey'),
    organization=os.getenv('org')
)


while True:
    prompt = input("Ask a question about the article: ")


    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system", 
                    "content": f"You are a helpful assistant. Answer questions based on the following Wikipedia article about The Buddha:\n\n{article_text[:4000]}"
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=4096
        )
        
        print()
        print(response.choices[0].message.content)
        print()
        
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
