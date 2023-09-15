from turtle import distance
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)

temp_list = []

def scrape():
    headers = ["Star name", "distance", "mass", "radius"]
    soup = bs(browser.page_source, "html.parser")
    star_table = soup.find('table')
    table_rows = star_table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)


star_names = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][1])

df = pd.DataFrame(list(zip(star_names, distance, mass, radius)), columns = ["Star name", "distance", "mass", "radius"])
print(df)
df.to_csv('bright_stars.csv')