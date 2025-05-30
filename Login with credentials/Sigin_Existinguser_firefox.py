from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

# --- Credentials ---
EMAIL = "johnmason@gmail.com"
PASSWORD = "37ZRn7-Atm_3wc."

# --- Set up Firefox ---
options = FirefoxOptions()
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/115.0 Firefox/115.0")
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

try:
    # Open JCPenney website
    driver.get("https://www.jcpenney.com/")
    time.sleep(3)

    # Check the page title
    assert "JCPenney" in driver.title
    print("✅ JCPenney homepage loaded successfully.")

    wait = WebDriverWait(driver, 15)

    # Click "Sign In" on account menu
    sign_in_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//p[@data-automation-id="acc-info-state" and text()="Sign In"]'))
    )
    sign_in_button.click()
    print("✅ Clicked on Sign In button successfully.")
    time.sleep(2)

    # Click actual "Sign In" in the modal/panel
    sign_in_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="atPanelContent"]/div/div/div[3]/div[2]/button/span')))
    sign_in_link.click()
    print("✅ Clicked on Sign In panel button successfully.")

    # Fill in credentials
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "loginEmail")))
    email_input.send_keys(EMAIL)
    print("✅ Email populated successfully.")
    time.sleep(2)

    password_input = driver.find_element(By.ID, "signin-password")
    password_input.send_keys(PASSWORD)
    print("✅ Password entered successfully.")

    # Submit form
    sign_in_submit = driver.find_element(By.XPATH, '//*[@id="atPanelContent"]/div/div[1]/div[2]/form/div/div[5]/button/span')
    sign_in_submit.click()

    # Wait for greeting
    greeting = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//button[@data-automation-id="account-icon-button"]//span[contains(text(), "Hi")]')
    ))
    greeting_text = greeting.text
    assert "Hi John" in greeting_text, f"❌ Greeting text not found. Found: '{greeting_text}'"
    print("✅ Login successful. Greeting found:", greeting_text)

    # Screenshot
    driver.save_screenshot("jcpenney_login_success.png")

except Exception as e:
    print("❌ An error occurred:", e)
    driver.save_screenshot("jcpenney_error.png")

finally:
    driver.quit()
