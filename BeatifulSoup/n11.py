
import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class":"column"},limit =50)

count = 1

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"proDetail"}).find("del").text
    newprice = li.find("div",{"class":"proDetail"}).find("ins").text
    print(f"{count} - Product Name: {name}\nProduct Link: {link}\nOld Price: {oldprice}\nNew Price: {newprice}\n-----------------------------")
    count +=1
# print(list)