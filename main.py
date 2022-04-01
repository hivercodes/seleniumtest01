from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://orteil.dashnet.org/experiments/cookie/")

while True:
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()
    money = int(driver.find_element(By.ID, "money").text)
    store = driver.find_element(By.ID, "store").text
    storedata = store.split("\n")
    things = []
    price = []
    for i in range(len(storedata)):
        if i % 2 == 0:
            things.append(storedata[i])

    for l in things:
        split_tp_price = l.split(" ")[-1]
        price.append(int(split_tp_price.replace(",", "")))
        print(split_tp_price)

    store_options = {
        price[7]: '//*[@id="buyCursor"]',
        price[6]: '//*[@id="buyGrandma"]',
        price[5]: '//*[@id="buyFactory"]',
        price[4]: '//*[@id="buyMine"]',
        price[3]: '//*[@id="buyShipment"]',
        price[2]: '//*[@id="buyAlchemy lab"]',
        price[1]: '//*[@id="buyPortal"]',
        price[0]: '//*[@id="buyTime machine"]'
    }
    for key in store_options:
        time.sleep(0.1)
        buy = driver.find_element(By.XPATH, store_options[key])
        buy.click()
