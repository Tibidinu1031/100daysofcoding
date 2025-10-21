import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
html = response.text

#print(html)

soup = BeautifulSoup(html, "html.parser")

myLinks = soup.find_all("span", {"class": "titleline"})

#print("Total links:::::::::::::::::::::::::", len(myLinks))

things = ["replit", "python", "coding", "llms", "work", "brain", "apple"]

for link in myLinks:
    text = link.text
    textList = text.split()
    containsWord = False
    for word in textList:
        if word.lower() in things:
            containsWord = True
    if containsWord:
        print(text)
        myLink = link.find_all("a")
        print(myLink[0]['href'])
        print()


#<span class="titleline"><a href="https://kyutai.org/next/codec-explainer">Neural audio codecs: how to get audio into LLMs</a><span class="sitebit comhead"> (<a href="from?site=kyutai.org"><span class="sitestr">kyutai.org</span></a>)</span></span>