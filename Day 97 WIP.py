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

headers = {
    'User-Agent': f'MyWikipediaBot/1.0 ({email}) Python/3.x'
}

url = "https://en.wikipedia.org/wiki/The_Buddha"

response = requests.get(url, headers=headers)
html = response.text

print(html)

soup = BeautifulSoup(html, "html.parser")

text = soup.get_text()
print(text)


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
