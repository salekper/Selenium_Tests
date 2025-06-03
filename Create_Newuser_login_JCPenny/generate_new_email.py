from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import undetected_chromedriver as uc

# Set Chrome options (optional)
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
# options.add_argument("--headless")  # Uncomment this if you want to run without UI

# Start Chrome (match version to your local Chrome install)
driver = uc.Chrome(version_main=136, options=options)

try:
    # Open mail.tm
    driver.get("https://mail.tm")

    # Wait for the email to generate (allow a few seconds)
    time.sleep(5)

    # Locate the email address field
    email_field = driver.find_element(By.CSS_SELECTOR, "#Dont_use_WEB_use_API_OK")

    # Get the generated email
    generated_email = email_field.get_attribute("value")
    print("******************************************Generated email:", generated_email)

finally:
    # Clean up
    driver.quit()
