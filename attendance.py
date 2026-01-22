import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Settings
URL = "url"
STUDENT_ID = "nic"

def start_automation():
    options = Options()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    
    try:
        print("Step 1: Website ekata yanawa")
        driver.get(URL)
        wait = WebDriverWait(driver, 20)

        # 1. NIC/ID eka type kirima
        print(f"Step 2: ID {STUDENT_ID} type karanawa")
        input_field = wait.until(EC.presence_of_element_located((By.ID, "nic")))
        input_field.clear()
        input_field.send_keys(STUDENT_ID)

        # 2. Search Classes button eka click kirima
        print("Step 3: Search Classes button eka click karanawa")
        search_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        driver.execute_script("arguments[0].click();", search_btn)
        
        # Aluth button eka enakan podi welawak inna
        time.sleep(2)

        # 3. Mark Attendance button eka hoyala click kirima
        print("Step 4: MARK ATTENDANCE button eka hoyanawa")
        # Image eke thiyana widiyata meka click karamu
        mark_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Mark Attendance')]")))
        
        # Button eka thiyana thanata scroll karanna
        driver.execute_script("arguments[0].scrollIntoView();", mark_btn)
        time.sleep(1)
        
        # Anthima click eka
        driver.execute_script("arguments[0].click();", mark_btn)
        
        print("\n✅ SUCCESS! Mark Attendance button eka click kala.")

    except Exception as e:
        print(f"\n❌ Error ekak awa: {e}")
    finally:
        print("\nScan iwarai. Browser eka winadiyakata passe wahenawa.")
        time.sleep(60)
        driver.quit()

if __name__ == "__main__":
    start_automation()