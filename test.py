import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


try:
    df = pd.read_excel('contacts.xlsx')
    phone_numbers = df['Phone'].astype(str).tolist()
    print(f"Loaded {len(phone_numbers)} numbers from Excel.")
except Exception as e:
    print(f"Error: {e}")
    exit()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://web.whatsapp.com")

wait = WebDriverWait(driver, 45)

print("\n1. Scan the QR Code.")
input("2. Press Enter HERE after chats load...")

print("Starting in 3 seconds... CLICK inside the WhatsApp page NOW!")
time.sleep(3)

for group_index in range(30):
    start = group_index * 100
    current_batch = phone_numbers[start : start + 100]
    
    if not current_batch:
        break

    try:
        print(f"\n--- Creating Group {group_index + 1} ---")


        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('n').key_up(Keys.ALT).key_up(Keys.CONTROL).perform()
        time.sleep(2)


        print("Navigating to 'New group' via Tab keys...")
        tab_actions = ActionChains(driver)
        for _ in range(5):
            tab_actions.send_keys(Keys.TAB)
            time.sleep(0.2)
        tab_actions.send_keys(Keys.ENTER).perform()
        time.sleep(2)

        
        for number in current_batch:
            try:
        
                search_xpath = '//div[@contenteditable="true"][@data-tab="3"] | //input[@placeholder="Search name or number"]'
                search_box = wait.until(EC.presence_of_element_located((By.XPATH, search_xpath)))
                
                search_box.send_keys(number)
                time.sleep(1.5) 
                search_box.send_keys(Keys.ENTER)
                
        
                search_box.send_keys(Keys.CONTROL + "a")
                search_box.send_keys(Keys.BACKSPACE)
            except:
                continue

        
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

        
        name_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')))
        name_box.send_keys(f"Group {group_index + 1}")
        time.sleep(1)
        name_box.send_keys(Keys.ENTER)
        
        print(f"Group {group_index + 1} created successfully!")
        
        
        pause = random.randint(20, 40)
        print(f"Waiting {pause}s...")
        time.sleep(pause)

    except Exception as e:
        print(f"Failed: {e}")
        driver.refresh()
        time.sleep(10)

print("\nAll done.")
driver.quit()