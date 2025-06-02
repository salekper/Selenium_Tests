from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# --- Credentials ---
EMAIL = "shweta@empirecovers.com"
PASSWORD = "Test123"

# --- Set up Chrome ---
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # Uncomment this if you want to run without UI

# Start Chrome (match version to your local Chrome install)
driver = uc.Chrome(version_main=136, options=options)


try:
    # Open Empire website
    driver.get("https://www.empirecovers.com/")
    time.sleep(3)  # Let the page load
    print("Empire page loaded successfully")
except Exception as e:
    print("❌ An error occurred:", e)
try:
    element = driver.find_element(By.CSS_SELECTOR, "div.header-logo.order-1.col-auto")
    print("✅ Logo container is present on the page.")
except NoSuchElementException:
    print("❌ Logo container is NOT present on the page.")

    time.sleep(2)

#

wait = WebDriverWait(driver, 10)
Account_button = wait.until(
EC.element_to_be_clickable(
            (By.XPATH, '/html/body/header/div[2]/div[1]/div[2]/nav/ul/li[6]/a/span[1]')
        )
    )

    # Click the "Account" button

Account_button.click()
print("✅ Clicked on Sign In button successfully.")
time.sleep(2)


# --- Enter email and password ---
email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
email_input.send_keys(EMAIL)
print("✅ email populated successfully.")

time.sleep(2)

password_input = driver.find_element(By.ID, "Password")
password_input.send_keys(PASSWORD)
print("✅ password entered successfully.")

# --- Click Log in button ---

Log_in_button = driver.find_element(By.XPATH, '/html/body/main/div/section/div[1]/form/fieldset/div[3]/div[2]/input')

Log_in_button.click()

# Validate for account user name "SHWETA"
try:
    element = driver.find_element(By.CSS_SELECTOR, "span.d-xl-none.d-xga-inline.pl-1")
    element_text = element.text.strip()

    # Case-insensitive check
    if "SHWETA".lower() == element_text.lower():
        print("✅ Text 'SHWETA' matches the element text (case-insensitive).************************LOG IN SUCCESS***************")
    else:
        print("❌ Text 'SHWETA' does NOT match the element text.")
except NoSuchElementException:
    print("❌ Element not found.")
except Exception as e:
    print("❌ An error occurred:", e)

finally:
    driver.quit()
