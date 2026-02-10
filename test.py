from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

input("Scan QR Code and press Enter...")

def random_delay():
    time.sleep(random.randint(5, 12))

for group_index in range(30):
   
    driver.find_element(By.XPATH, '//div[@title="New chat"]').click()
    random_delay()

   
    driver.find_element(By.XPATH, '//div[@title="New group"]').click()
    random_delay()

    for i in range(100):
        number = phone_numbers[group_index*100 + i]

        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(number)
        time.sleep(2)

        search_box.send_keys(Keys.ENTER)
        random_delay()

   
    driver.find_element(By.XPATH, '//span[@data-icon="arrow-forward"]').click()
    random_delay()

   
    group_name = f"Group_{group_index+1}"
    name_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')
    name_box.send_keys(group_name)

    driver.find_element(By.XPATH, '//span[@data-icon="checkmark"]').click()
    random_delay() 