import os
from time import sleep
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

mushrooms = ["maitake_mushroom", "matsutake_mushroom", "shiitake_mushroom", "beech_mushroom",
             "winter_mushroom", "king_trimpet_mushroom", "cloud_ear_mushroom", "closed_cup_mushroom", "truffle"]
pwd = os.getcwd()

for dir in mushrooms:
    os.makedirs(f"{pwd}\\{dir}", exist_ok=True)

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.use_chromium = True
browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

url = "https://www.google.co.jp/imghp?hl=ja"
browser.get(url)

keywords = ["舞茸", "松茸", "椎茸", "しめじ", "えのき", "エリンギ", "木耳", "マッシュルーム", "トリュフ"]

for keyword in keywords:
    kw_search = browser.find_element_by_css_selector(
        "#sbtc > div > div.a4bIc > input")
    kw_search.send_keys(keyword)
    kw_search.send_keys(Keys.ENTER)
    cur_url = browser.current_url
    res = requests.get(cur_url)
    soup = BeautifulSoup(res.text, "html.parser")
    img_tags = soup.find_all("img", limit=10)
    img_urls = []

    for img_tag in img_tags:
        img_urls.append(img_tag.get("src"))

    i = 1
    for img_url in img_urls:
        try:
            src = requests.get(img_url)
            with open(f"maitake_mushroom/maitake_mushroom_img_{str(i)}.jpg", "wb") as img:
                img.write(src.content)
            i += 1
            sleep(0.1)
        except:
            pass

    sleep(3)
    browser.get(url)
