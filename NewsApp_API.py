import requests

api="f0e03e17d3374a44ba006b00682c9b4e"
url=f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey={api}"
print(url)
r=requests.get(url)
data=r.json()
articles=data["articles"]
for index,article in enumerate(articles):#for article in articles
    print(index+1,article["title"],article["url"])
    print("******************************\n")