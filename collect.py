from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title':[],'price':[],'link':[]}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        t = soup.find(class_="KzDlHZ")
        title = t.get_text()
        p = soup.find("div",attrs={"class":"_4b5DiR"})
        cleaned_p = p.get_text()
        price = cleaned_p.replace('â‚¹', '').replace(',', '')
        l = soup.find(class_="CGtC98")
        link = "https://www.flipkart.com"+l['href']
        
        d["title"].append(title)
        d["price"].append(price)
        d["link"].append(link)
    except Exception as e:
        print(e)

df = pd.DataFrame(data=d)
df.to_csv("data.csv")
