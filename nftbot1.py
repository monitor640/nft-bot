from selenium import webdriver
import time
import pyautogui,sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import numpy as np
from scraper import scraper
import PySimpleGUI as sg


layout = [[sg.Text('Sisesta netileht ja failinimi')],
                 [sg.Text('Netileht', size=(15, 1)),sg.InputText()],
                 [sg.Text('Failinimi', size=(15, 1)),sg.InputText()],
                 [sg.Submit(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

event, values = window.read()
window.close()

netileht=values[0]
scrapetudfail=values[1]
options1=webdriver.ChromeOptions()
options1.add_argument(r"--user-data-dir=C:\\Users\\Kasutaja\\AppData\\Local\\Google\\Chrome\\User Data" )
options1.add_argument(r'--profile-directory=Profile 1')
driver=webdriver.Chrome(executable_path=r'C:\Users\Kasutaja\progekodu\chromedriverid\chromedriver.exe', options = options1)
driver.get(netileht)
connectwallet=driver.find_element_by_xpath("//button[contains(., 'Connect Wallet')]")
connectwallet.click()
phantom=driver.find_element_by_xpath("//button[contains(., 'Phantom')]")
phantom.click()
time.sleep(2)
pyautogui.write("foxinabox")
pyautogui.moveTo(1706,683)
pyautogui.click()
time.sleep(5)
pyautogui.click()
time.sleep(1)
last_height=0
new_height=0
while True:
    # Scroll down to bottom
    driver.find_element_by_xpath('//body').send_keys(Keys.CONTROL+Keys.END)

    # Wait to load page
    time.sleep(2)


    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    # break condition
    if new_height == last_height:
        break
    last_height = new_height
scraper(scrapetudfail,driver)
#for x in nft_list:
#    rank=
#    fairvalue=1266-(81.25*(np.log(575*rank-14100)))
#https://alpha.art/collection/degods
