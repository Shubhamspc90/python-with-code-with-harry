
import requests # type: ignore

r=requests.get("https://www.google.com")
print(r.text)

