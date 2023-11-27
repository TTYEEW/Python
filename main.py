# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import math
from selenium import webdriver
import time

path = r"C:\Python"
projectname = "dataset"
folders = \
["1",
 "2",
 "3",
 "4",
 "5"]

def Folder():
    fullPath = os.path.join(path, projectname)
    if not os.path.exists(fullPath):
        os.mkdir(fullPath)
    for f in folders:
        folder = os.path.join(fullPath, f)
        if not os.path.exists(folder):
            os.mkdir(folder)

def parse_reviews(rating, soup):
    reviews = soup.findAll("div", class_= f"lenta-card")
    review_texts = []
    for review in reviews:
        try:
            rate = math.floor(float(review.find("span", class_=f"lenta-card__mymark").get_text(strip=True)))
        except AttributeError: break
        name_book = review.find("a", class_=f"lenta-card__book-title").text.strip()
        review_text = review.find("div", {'id':"lenta-card__text-review-escaped"}).get_text(strip=True)
        if rate == rating:
            review_texts.append(name_book + "\n" + review_text)
    return review_texts

def write_reviews(reviews, rating, count):
    for review_text in reviews:
        if count < 1000:
            with open(fr"C:\Python\dataset\{rating}\{count:04}.txt", "w", encoding="utf-8") as file:
                file.write(review_text)
            count += 1
        else:
            break
    return count

def main():
    list = [5,4,3,2,1]
    for k in list:
        count = 0
        for i in range(1, 2):
            url = f"https://www.livelib.ru/reviews/~{i}#reviews"
            driver = webdriver.Chrome()
            driver.get(url)
            assert "No results found." not in driver.page_source
            time.sleep(3)
            src = driver.page_source
            driver.close()
            soup = BeautifulSoup(src, "lxml")
            review = parse_reviews(k, soup)
            count = write_reviews(review, k, count)
        print(f"{k}: {count}")
    return 0

if __name__ == '__main__':
    Folder()
    main()