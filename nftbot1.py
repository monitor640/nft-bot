from selenium import webdriver
import time
import pyautogui,sys
from selenium.webdriver.chrome.options import Options
from scraper import scraper

netileht="https://alpha.art/collection/solstead"
scrapetudfail="data2.csv"
options1=webdriver.ChromeOptions()
options1.add_argument(r"--user-data-dir=C:\\Users\\Kasutaja\\AppData\\Local\\Google\\Chrome\\User Data" )
options1.add_argument(r'--profile-directory=Profile 1')
driver=webdriver.Chrome(executable_path=r'C:\Users\Kasutaja\progekodu\chromedriverid\chromedriver.exe', options = options1)
driver.get(netileht)
connectwallet=driver.find_element_by_xpath("//button[contains(., 'Connect Wallet')]")
connectwallet.click()
phantom=driver.find_element_by_xpath("//button[contains(., 'Phantom')]")
phantom.click()
time.sleep(1)
pyautogui.write("foxinabox")
pyautogui.moveTo(1706,683)
pyautogui.click()
scraper(scrapetudfail,driver)
