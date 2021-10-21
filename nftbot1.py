from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
browser=webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://alpha.art/")
time.sleep(2)
connectwallet=browser.find_element_by_xpath("//button[contains(., 'Connect Wallet')]")
time.sleep(1)
connectwallet.click()
time.sleep(1)
phantom=browser.find_element_by_xpath("//button[contains(., 'Phantom')]")
phantom.click()
