import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = "https://news.ycombinator.com/"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Grab all titleline spans
titlelines = soup.find_all("span", class_="titleline")

matches = 0
for span in titlelines:
    text = span.get_text(strip=True).lower()
    if "python" in text or "replit" in text or "Show HN" in text:
        matches += 1
        # Try to get the link if it exists
        a_tag = span.find("a")
        href = a_tag.get("href", "No link") if a_tag else "No link"
        print(text)
        print(href)
        print("\n" + "-"*70 + "\n")

if matches == 0:
    print("No matching titles found.")
