import requests

# query=input("What type of news you are interested today?")

# api="57d482e7810e4c5eae8e9c19ae456f2b"

url ="https://newsapi.org/v2/everything?q=apple&from=2026-06-19&to=2026-06-19&sortBy=popularity&apiKey=57d482e7810e4c5eae8e9c19ae456f2b"

print(url)
r=requests.get(url)
data=r.json()
articles=data["articles"]

for index,article in enumerate( articles):
    print(index+1,article["title"],article["url"])
    print("\n ******************************************************************************************\n")