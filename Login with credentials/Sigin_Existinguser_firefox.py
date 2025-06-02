from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

# --- Credentials ---
EMAIL = "shweta@empirecovers.com"
PASSWORD = "Test123"

# --- Set up Firefox ---
options = FirefoxOptions()
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/115.0 Firefox/115.0")
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

try:
    # Open Empire Covers website
    driver.get("https://www.empirecovers.com/")
    time.sleep(3)
except Exception as e:
    print("❌ An error occurred:", e)
    # Check the page title
try:
    assert "Empire covers" in driver.title
    print("✅ Empire Covers homepage loaded successfully.")
except Exception as e:
    print("❌ An error occurred:", e)
    wait = WebDriverWait(driver, 15)

    # Click "Account" on main menu    
try:
    Account_button = driver.find_element(By.XPATH, '/html/body/header/div[2]/div[1]/div[2]/nav/ul/li[6]/a/span[1]')
    Account_button.click()
    time.sleep(2)
except Exception as e:
    print("❌ An error occurred:", e)   

    # Fill in credentials
try:
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
    email_input.send_keys(EMAIL)
    print("✅ Email populated successfully.")
    time.sleep(2)

    password_input = driver.find_element(By.ID, "Password")
    password_input.send_keys(PASSWORD)
    print("✅ Password entered successfully.")
except Exception as e:
    print("❌ An error occurred:", e)
    # Submit form
    Log_in = driver.find_element(By.XPATH, '/html/body/main/div/section/div[1]/form/fieldset/div[3]/div[2]/input')
    Log_in.click()

    # Validate for account user name "XX"
try:
    username = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="user-menu-btn"]/span[2]')
    ))
    time.sleep(2)
    # Screenshot
    driver.save_screenshot("Empire_login_success.png")
    print("*****************✅ Logged in successfully.***************************")
except Exception as e:
    print("❌ An error occurred:", e)
    driver.save_screenshot("jcpenney_error.png")

finally:
    driver.quit()
