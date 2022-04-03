from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://orteil.dashnet.org/experiments/cookie/")

while True:
    cookie = driver.find_element(By.ID, "cookie")
    clicks = 0
    while clicks < 500:
        cookie.click()
        clicks = clicks + 1
    clicks = 0

    store_list = ['//*[@id="buyTime machine"]',
                  '//*[@id="buyPortal"]',
                  '//*[@id="buyAlchemy lab"]',
                  '//*[@id="buyShipment"]', '//*[@id="buyMine"]',
                  '//*[@id="buyFactory"]',
                  '//*[@id="buyGrandma"]',
                  '//*[@id="buyCursor"]'
                  ]

    for key in range(len(store_list)):
        time.sleep(0.1)
        buy = driver.find_element(By.XPATH, store_list[key])
        buy.click()
