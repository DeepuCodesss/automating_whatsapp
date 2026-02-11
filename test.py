import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

script_dir = os.path.dirname(os.path.abspath(__file__))
session_path = os.path.join(script_dir, "whatsapp_session")
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={session_path}")
chrome_options.add_argument("--profile-directory=Default")

try:
    df = pd.read_excel('contacts.xlsx')
    phone_numbers = df['Phone'].astype(str).tolist()
    print(f"Loaded {len(phone_numbers)} numbers.")
except Exception as e:
    print(f"Error: {e}")
    exit()

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver, 45)

input("\nScan QR if needed. Press Enter after chats load...")
time.sleep(3)

for group_index in range(30):
    start = group_index * 100
    current_batch = phone_numbers[start : start + 100]
    if not current_batch: break
    try:
        print(f"Creating Group {group_index + 1}...")
        actions = ActionChains(driver)
        
        actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('n').key_up(Keys.ALT).key_up(Keys.CONTROL).perform()
        time.sleep(2)

        for _ in range(10):
            actions.send_keys(Keys.TAB).perform()
            time.sleep(0.4)
            active = driver.switch_to.active_element
            if "New group" in (active.text or active.get_attribute("innerText")):
                actions.send_keys(Keys.ENTER).perform()
                break
        
        time.sleep(3) 
        
        for number in current_batch:
            try:
                found_box = False
                for _ in range(5): 
                    actions.send_keys(Keys.TAB).perform()
                    time.sleep(0.3)
                    active = driver.switch_to.active_element
                    if active.get_attribute("role") == "textbox" or active.tag_name == "input":
                        active.send_keys(number)
                        time.sleep(2.0)
                        active.send_keys(Keys.ENTER)
                        time.sleep(1.5)
                        found_box = True
                        break
                
                if not found_box:
                    print(f"Skipping {number}, search bar not sensed.")
            except: continue
            
        try:
            next_btn = driver.find_element(By.XPATH, '//span[@data-icon="arrow-forward"]')
            next_btn.click()
        except:
            actions.send_keys(Keys.ENTER).perform()
            
        time.sleep(2)
        name_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')))
        name_box.send_keys(f"Group {group_index + 1}")
        name_box.send_keys(Keys.ENTER)
        
        print(f"Group {group_index + 1} Done!")
        time.sleep(random.randint(20, 40))
    except Exception as e:
        print(f"Failure: {e}")
        driver.refresh()
        time.sleep(10)

driver.quit()