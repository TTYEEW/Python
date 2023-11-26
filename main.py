import os
from bs4 import BeautifulSoup
import requests

url = "https://www.livelib.ru/reviews/~1#reviews"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

path = r"C:\Users\uwnik\OneDrive\Рабочий стол"
projectname = "dataset"
folders = \
["0",
 "1",
 "2",
 "3",
 "4",
 "5"]

fullPath = os.path.join(path, projectname)
if not os.path.exists(fullPath):
    os.mkdir(fullPath)
for f in folders:
    folder = os.path.join(fullPath, f)
    if not os.path.exists(folder):
        os.mkdir(folder)

def parse_reviews():
    reviews = soup.findAll("div", class_= f"lenta-card")
    review_texts = []
    for review in reviews:
        name_book = review.find("a", class_=f"lenta-card__book-title").text.strip()
        review_text = review.find("div", id_="lenta-card__text-review-full").text.strip()
        review_texts.append(review_text)
    return review_texts
