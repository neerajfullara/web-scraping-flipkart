from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "Laptop"

for i in range(1,20):
    driver.get(f"https://www.flipkart.com/search?q={query}&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&as-pos=2&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=d07df4cc-eb31-4f5b-b79f-a0b12c6b764d&as-searchtext=lap&as-searchtext=lap&page={i}")

    elems = driver.find_elements(By.CLASS_NAME, "tUxRFH")
    print(f"{len(elems)} elements found")
    for elem in elems:
        print(elem.text)
    # print(elem.get_attribute("outerHTML"))

    time.sleep(6)
    driver.close()