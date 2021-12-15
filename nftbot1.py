from selenium import webdriver
import time
import pyautogui,sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import numpy as np
from scraper import scraper
import pandas as pd
import PySimpleGUI as sg
import csv
from rarityscraper import rarityscraper


layout = [[sg.Text('Sisesta netileht ja failinimi')],
                 [sg.Text('Netileht', size=(15, 1)),sg.InputText()],
                 [sg.Text('Failinimi', size=(15, 1)),sg.InputText()],
                 [sg.Text('Failinimirarity', size=(15, 1)),sg.InputText()],
                 [sg.Submit(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

event, values = window.read()
window.close()

netileht=values[0]
scrapetudfail=values[1]
rarityscrapetud=values[2]
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
rarityscraper("https://howrare.is/solsocks", rarityscrapetud)
viimane_item=len(pd.read_csv(rarityscrapetud))
print(viimane_item)
hinnad=[]
for rida in scrapetudfail:
    ridalist=rida.split(" ")
    hind=ridalist[-1]
    hinnad.append(hind)
odavaim_hind=min(hinnad)


with open("rariscraper.txt", "w") as my_output_file:
    with open(rarityscrapetud, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
my_output_file=open("rariscraper.txt","r")
loendur2=0
for x in my_output_file:
    print(x)
    a=x.split(" ")
    print(a)
    if loendur2!=0:
        rank=a[1]
        print(rank)
        fairvalue=(1266-(81.25*(np.log(575*int(rank)-14100))))-(1266-(81.25*(np.log(575*int(viimane_item)-14100)-int(odavaim_hind))))
        print(fairvalue)
    loendur2+=1
my_output_file.close()
#https://alpha.art/collection/degods
