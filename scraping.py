from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

link = "https://bit.ly/scrapingtry"
driver.set_window_size(1300, 800)
driver.get(link)
time.sleep(5)

driver.save_screenshot("home.png")
content = driver.page_source
driver.quit()

data = BeautifulSoup(content, "html.parser")
print(data.encode("utf-8"))

i = 1

list_judul, list_harga = [], []
for area in data.find_all("div", class_ = "psw-product-tile psw-interactive-root") : 
    print("Proses data ke-" +str(i))
    judul = area.find("span", class_ = "psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2"). get_text()
    harga = area.find("span", class_ = "psw-m-r-3").get_text()
    print(judul)
    print(harga)

    list_judul.append(judul)
    list_harga.append(harga)
    i+=1

df = pd.DataFrame({"Judul" : list_judul, "Harga" : list_harga})
writer = pd.ExcelWriter("Hasil Scraping.xlsx")
df.to_excel(writer, "Sheet1", index=False)
writer._save()