from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Product import Product
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.sample.com")
print(driver.title)

driver.find_element_by_id('cboxClose').click()
item_names = driver.find_elements_by_class_name('item-name')
item_prices = driver.find_elements_by_class_name('item-price')
product_units = driver.find_elements_by_class_name('productUnit')

productHashTable = {}
count = 0
for item in item_names:
    productHashTable[count] =  Product(item.text,0,0)
    count = count+1

count = 0
for item in item_prices:
    product = productHashTable[count]
    product.price = item.text
    count = count + 1

count = 0
for item in product_units:
    product = productHashTable[count]
    product.unit = item.text
    count = count + 1

for a in productHashTable.keys():
    productHashTable[a].toString()
