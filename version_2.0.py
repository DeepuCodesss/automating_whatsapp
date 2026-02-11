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

input("\nOpen Group Info. Press Enter here...")

for i in range(0, len(phone_numbers), 3):
    current_batch = phone_numbers[i:i+3]
    if not current_batch: break
    
    try:
        actions = ActionChains(driver)
        print(f"\n--- Batch: {current_batch} ---")

        for _ in range(30):
            actions.send_keys(Keys.TAB).perform()
            time.sleep(0.2)
            active = driver.switch_to.active_element
            if "Add" in (active.text or active.get_attribute("innerText") or ""):
                actions.send_keys(Keys.ENTER).perform()
                break
        
        time.sleep(3)

        for number in current_batch:
            for _ in range(15):
                actions.send_keys(Keys.TAB).perform()
                time.sleep(0.2)
                active = driver.switch_to.active_element
                if active.get_attribute("role") == "textbox" or active.tag_name == "input":
                    active.send_keys(number)
                    time.sleep(2.5)
                    active.send_keys(Keys.ENTER)
                    time.sleep(1.5)
                    break

        print("Clicking Green Tick...")
        tick_xpath = '//*[@aria-label="Confirm"]'
        tick_btn = wait.until(EC.element_to_be_clickable((By.XPATH, tick_xpath)))
        tick_btn.click()
        print("Green Tick Clicked!")

        time.sleep(2)

        final_xpath = '//*[text()="Add members"]'
        final_btn = wait.until(EC.element_to_be_clickable((By.XPATH, final_xpath)))
        final_btn.click()
        print("Final 'Add members' confirmed!")
        
        print("Waiting 30 seconds for next batch...")
        time.sleep(30)

    except Exception as e:
        print(f"Error: {e}")
        driver.refresh()
        time.sleep(10)

driver.quit()