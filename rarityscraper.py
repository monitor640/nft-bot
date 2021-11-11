def rarityscraper(veebileht, fail):
    from parse import search
    from selenium import webdriver
    import time
    import pandas as pd

    driver = webdriver.Chrome(executable_path=r"C:\Users\Kasutaja\progekodu\chromedriverid\chromedriver.exe")
    loendur=0

    while True:

        try:
            driver.get(veebileht+"?page="+str(loendur)+"&ids=&sort_by=rank")
            print(driver.title)
            time.sleep(5)
            lingid = driver.find_elements_by_class_name('nft-details')
            lingid.pop(0)
            lingid.pop(0)
            nft_list = []

            for el in lingid:
                nimi = el.find_element_by_xpath('./h3').text
                #hind = el.find_element_by_xpath('.//div[2]/div/h3').text
                nft = {
                "nimi":nimi,
                #"hind":hind
                }
                nft_list.append(nft)

            loendur+=1
        except:
            driver.quit()
            break
    df = pd.DataFrame(nft_list)

    df.to_csv(fail)
rarityscraper("https://howrare.is/degenapes", "data2.csv")
