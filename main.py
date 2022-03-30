from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.com/UGREEN-Coupler-Ethernet-Extender-Connector/dp/B016B13U9Y/ref=sr_1_3?crid=1KU8LQFN71VHU&keywords=ethernet+extender&qid=1648573618&sprefix=%2Caps%2C145&sr=8-3")
price = driver.find_element(By.XPATH, '//*[@id="corePrice_feature_div"]/div/span/span[2]')
print(price.text)
driver.close()