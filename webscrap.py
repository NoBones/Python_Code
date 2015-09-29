import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA"
r = requests.get(url)

soup = BeautifulSoup(r.content)


links = soup.find_all("a")
for link in links:
    #if "http" || "https" in link.get("href"):
        print("<a href='%s'> %s</a>" %(link.get("href"), link.text))
    
g_data = soup.find_all("div", {"class": "info"})
for item in g_data:
    #print(item.contents[0].text)  #name of shop
    print(item.contents[0].find_all("a", {"class": "business-name"})[0].text) # business name
    #print(item.contents[1].find_all("p", {"class": "adr"})[0].text) #address
    try:
        print(item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text)
    except:
        pass
    try:
        print(item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text.
        replace(',', ':'),item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text,
        item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text)
    except:
        pass
    try:
        print(item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text)
    except:
        pass
    try:
        print(item.contents[1].find_all("div", {"itemprop": "telephone"})[0].text)
    except:
        pass
    
    