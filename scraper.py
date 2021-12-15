def scraper(fail,driver):
    from parse import search
    from selenium import webdriver
    import time
    import pandas as pd

    #driver = webdriver.Chrome(executable_path=r"C:\Users\Kasutaja\progekodu\chromedriverid\chromedriver.exe")

    #driver.get(veebileht)
    print(driver.title)
    time.sleep(5)
    lingid = driver.find_elements_by_class_name('group ')
    lingid.pop(0)
    lingid.pop(0)

    nft_list = []

    for el in lingid:
        nimi = el.find_element_by_xpath('.//div[2]/h3').text
        hind = el.find_element_by_xpath('.//div[2]/div/h3').text
        nimi = nimi[nimi.find("#"):]
        nft = {
            "nimi":nimi,
            "hind":hind
        }
        nft_list.append(nft)
    driver.quit()
    df = pd.DataFrame(nft_list)

    df.to_csv(fail, index= False)