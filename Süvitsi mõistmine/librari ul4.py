from bs4 import BeautifulSoup
import requests


url = "https://news.ycombinator.com/"
response = requests.get(url)
html=response.text

soup=BeautifulSoup(html,"html.parser")

titles= soup.find_all("span", class_="titleline")

print("pealkirjad:")

for indexx, title in enumerate(titles[:10], start=1):
    print(indexx, title.get_text())