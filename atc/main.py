import requests
from bs4 import BeautifulSoup

URL = "https://atcoder.jp/users/ymsksky/history"

page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
lines = soup.find("tbody").find_all("tr")

for line in lines:
    elements = line.find_all("td")
    date: str = elements[0].get_text()[:-14]
    rate: str = elements[4].get_text()
    if not rate.isdigit():
        continue
    year, month, day = map(int, date.split("-"))
    rate = int(rate)
    print(f"{year:04d}", f"{month:02d}", f"{day:02d}", f"{rate:4}")
