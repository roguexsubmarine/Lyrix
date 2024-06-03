import requests
from bs4 import BeautifulSoup
import re

url = "https://genius.com/Clairo-softly-lyrics"
res = requests.get(url)
htmlData = res.content

parsedData = BeautifulSoup(htmlData, "lxml")
# print(parsedData.prettify())

pd = parsedData.find_all(class_="kUgSbL")

# removing whitespace
ly = re.sub(r"<[^>]+>", "\n", str(pd))
lyrics = ly.splitlines()
for lyric in lyrics:
    lyric.replace("\n", "")

lyrics = list(filter(None, lyrics))

#printing in terminal
for lyric in lyrics:
    print(lyric)
