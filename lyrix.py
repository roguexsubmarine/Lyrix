import requests
from bs4 import BeautifulSoup
import re

def get_links(prompt):
    
    url = "https://www.google.com/search?q=genius.com/"
    req = prompt.replace(' ', '')
    #print(url+req)

    res = requests.get(url+req)
    htmlData = res.content
    parsedData = BeautifulSoup(htmlData, "lxml")

    page_links = parsedData.find_all("a")
    links = []
    
    # filtering all valid links
    for link in page_links:
        if "genius.com/" in str(link) and "data-ved=" in str(link):
            links.append(link)

    # finding titles for links on first web page with hrefs
    # finding first 6 links
    iterator = 0
    for l in links:

        if(iterator > 5):
            break
        iterator += 1


        ll = str(l)
        # initializing substrings
        sub1 = ".com/"
        sub2 = "&amp"
 
        # getting index of substrings
        idx1 = ll.index(sub1)
        idx2 = ll.index(sub2)
 
        r = ''
        # getting elements in between
        for idx in range(idx1 + len(sub1), idx2):
            r = r + ll[idx]
 
        # printing options
        print( links.index(l) , " : " , r)
    
    # asking for choice
    choice = int(input("\n(default 0)\nEnter choice : ") or "0")
    return links[choice]["href"]

def get_lyrics(hlink):
    #url = "https://genius.com/Clairo-softly-lyrics"

    sub1 = "q="
    sub2 = "&"
    # getting index of substrings
    idx1 = hlink.index(sub1)
    idx2 = hlink.index(sub2)
    r = ''

    for idx in range(idx1 + len(sub1), idx2):
        r = r + hlink[idx]

    url = r
    print(url)
    
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
    return lyrics



# main program
prompt = input("Enter prompt : ")

url = get_links(prompt)
lyrics = get_lyrics(url)

# printing in terminal
for lyric in lyrics:
    print(lyric)
