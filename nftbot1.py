from selenium import webdriver
import time
import pyautogui,sys
from selenium.webdriver.chrome.options import Options
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
#driver=webdriver.Chrome(executable_path=r'C:\Users\Kasutaja\progekodu\chromedriverid\chromedriver.exe', options = options1)
driver = webdriver.Chrome()
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
