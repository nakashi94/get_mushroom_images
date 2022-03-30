from time import sleep
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.use_chromium = True
browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

url = "https://www.google.co.jp/imghp?hl=ja"
browser.get(url)

keywords = ["舞茸", "しめじ", "椎茸"]

for keyword in keywords:
    kw_search = browser.find_element_by_css_selector(
        "#sbtc > div > div.a4bIc > input")
    kw_search.send_keys(keyword)
    kw_search.send_keys(Keys.ENTER)
    cur_url = browser.current_url
    res = requests.get(cur_url)
    print(res)
    soup = BeautifulSoup(res.text, "html.parser")
    print(soup.find_all("img", limit=10))
    sleep(3)
    browser.get(url)
