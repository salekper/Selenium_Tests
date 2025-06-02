from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

import os
import time

# Define download folder
download_dir = os.path.join(os.path.expanduser("~"), "Downloads")

# Set Chrome options (optional)
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
# options.add_argument("--headless")  # Uncomment this if you want to run without UI

# Chrome options to enable PDF download
chrome_options = Options()
prefs = {
    "download.default_directory": download_dir,
    "plugins.always_open_pdf_externally": True,  # Disable preview
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)

# Setup Chrome
service = Service() 
driver = uc.Chrome(version_main=136, options=options)
#driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 20)  # increase wait time
actions = ActionChains(driver)

# 1. Set up download folder
download_folder = os.path.abspath("downloads")
os.makedirs(download_folder, exist_ok=True)


# 3. Open Empire website
try:
    
    driver.get("https://www.empirecovers.com/")
    driver.fullscreen_window()



    time.sleep(5)  # Let the page load

    print("✅  homepage loaded successfully.")

except Exception as e:
    print("❌ An error occurred:", e)

    time.sleep(2)

# Hover over the dropdown menu item "About"
menu = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div[2]/div[1]/div[2]/nav/ul/li[5]')))
actions.move_to_element(menu).perform()

# Wait and click the submenu item "Warranty Registration"
warranty_registration = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div[2]/div[1]/div[2]/nav/ul/li[5]/ul/li[1]/a/span')))
warranty_registration.click()

# 6. Click the download link

try:
 pdf_link = driver.find_element(By.LINK_TEXT, "DOWNLOAD OUR WARRANTY GUIDE")
 pdf_link.click()
 print("✅  Download button was found successfully.")

except Exception as e:
 print("❌ An error occurred:", e)

# 7. Wait for file to download
file_name = "Empire_Warranty_Auto_FINAL_08282023.pdf"
file_path = os.path.join(download_dir, file_name)

timeout = 30  # seconds
for _ in range(timeout):
    if os.path.exists(file_path):
        print(f"✅ File downloaded: {file_path}")
        break
    time.sleep(1)
else:
    print("❌ File download timed out.")

# shutdown
try:
    driver.quit()
except Exception as e:
    print(f"⚠️ Error during shutdown: {e}")