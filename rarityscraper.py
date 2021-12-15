def rarityscraper(veebileht, fail):
    from parse import search
    from selenium import webdriver
    import time
    import pandas as pd

    option = webdriver.ChromeOptions()
    chrome_prefs={}
    option.experimental_options["prefs"]=chrome_prefs
    chrome_prefs["profile.default_content_settings"]={"images":2}
    chrome_prefs["profile.managed_default_content_settings"]={"images":2}
    driver = webdriver.Chrome(executable_path=r"C:\Users\Kasutaja\progekodu\chromedriverid\chromedriver.exe",chrome_options=option)
    #driver = webdriver.Chrome()
    loendur=0
    nft_list = []

    while True:

        try:
            driver.get(veebileht+"?page="+str(loendur)+"&ids=&sort_by=rank")
            print(driver.title)
            time.sleep(1)
            lingid = driver.find_elements_by_class_name('item_stats')

            for el in lingid:
                nimi = el.find_element_by_xpath('.//div[1]/span').text
                rank = el.find_element_by_xpath('.//div[2]/span').text
                nft = {
                "nimi":nimi,
                "rank":rank
                }
                nft_list.append(nft)

            loendur+=1
        except:
            driver.quit()
            break
    df = pd.DataFrame(nft_list)

    df.to_csv(fail)
