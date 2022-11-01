from email import header
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pyvirtualdisplay import Display  
from tabulate import tabulate
display = Display(visible=0, size=(800, 600)) 
url = 'https://messari.io/asset/ethereum/markets'

display.start()

driver = webdriver.Firefox()
driver.get(url)

#tr.MuiTableRow-root:nth-child(2) > td:nth-child(1) ----> CSS Selector for exchange

#tr.MuiTableRow-root:nth-child(2) > td:nth-child(2) ----> CSS Selector for pair

#tr.MuiTableRow-root:nth-child(2) > td:nth-child(3) ----> CSS Selector for price

exchanges = []
pairs = []
prices = []

for count in range(1, 20):
    
    
    pair = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.MuiTableRow-root:nth-child(" + str(count) + ") > td:nth-child(2)")))
    if pair.text == "ETH\n/\nUSD":       
        pairs.append(pair.text)

        price = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.MuiTableRow-root:nth-child(" + str(count) + ") > td:nth-child(3)")))
        strippedDol = price.text.replace("$", "")
        strippedCom = strippedDol.replace(",", "")
        prices.append(strippedCom)

        exchange = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.MuiTableRow-root:nth-child(" + str(count) + ") > td:nth-child(1)")))
        exchanges.append(exchange.text)

#res = "\n".join("{} {}".format(x, y) for x, y in zip(exchanges, prices))
#print(res)

dict = {}

for key in exchanges:
    for value in prices:
        dict[key] = value
        prices.remove(value)
        break

[print(key, ":", value) for key, value in dict.items()]
print("")

max = max(dict, key=dict.get)
min = min(dict, key=dict.get)

print(f"Min price is: {dict[min]} at {min}")
print(f"Max price is: {dict[max]} at {max}")
print(f"Estimated profit: {float(dict[max]) - float(dict[min])}")
    

driver.quit()
display.stop()
    





    
