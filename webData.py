from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

scraped_data = []

def scrape():
    bright_star_table = soup.find("table",attrs={"class","wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in range(table_rows):
        table_cols = row.find_all('td')
        print(table_cols)

    for col_data in table_cols:

        print(col_data.text)
        