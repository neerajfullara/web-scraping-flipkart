from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "Laptop"
fileNo = 0
for i in range(1,20):
    driver.get(f"https://www.flipkart.com/search?q={query}&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&as-pos=2&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=d07df4cc-eb31-4f5b-b79f-a0b12c6b764d&as-searchtext=lap&as-searchtext=lap&page={i}")

    elems = driver.find_elements(By.CLASS_NAME, "CGtC98")
    print(f"{len(elems)} elements found")
    for elem in elems:
        # print(elem.text)
        d=elem.get_attribute("outerHTML")
        with open(f"data/{query}_{fileNo}.html","w",encoding='utf-8') as f:
            f.write(d)
            fileNo+=1

    time.sleep(4)
driver.close()