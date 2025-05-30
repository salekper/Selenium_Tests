from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Credentials ---
EMAIL = "johnmason@gmail.com"
PASSWORD = "37ZRn7-Atm_3wc."

# --- Set up Chrome ---
options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36")

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-quic')




# Correct WebDriver initialization
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open JCPenney website
    driver.get("https://www.jcpenney.com/")
    time.sleep(3)  # Let the page load

    # Check the page title
    assert "JCPenney" in driver.title
    print("✅ JCPenney homepage loaded successfully.")

except Exception as e:
    print("❌ An error occurred:", e)

    time.sleep(2)



wait = WebDriverWait(driver, 10)
sign_in_button = wait.until(
EC.element_to_be_clickable(
            (By.XPATH, '//p[@data-automation-id="acc-info-state" and text()="Sign In"]')
        )
    )

    # Click the "Sign In" button

sign_in_button.click()
print("✅ Clicked on Sign In button successfully.")
time.sleep(2)

# --- Click "Sign In" ---
sign_in_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="atPanelContent"]/div/div/div[3]/div[2]/button/span')))
sign_in_link.click()
print("✅ Clicked on Sign In button successfully.")

# --- Enter email and password ---
email_input = wait.until(EC.visibility_of_element_located((By.ID, "loginEmail")))
email_input.send_keys(EMAIL)
print("✅ email populated successfully.")

time.sleep(2)

password_input = driver.find_element(By.ID, "signin-password")
password_input.send_keys(PASSWORD)
print("✅ password entered successfully.")

# --- Click sign in button ---

sign_in_button = driver.find_element(By.XPATH, '//*[@id="atPanelContent"]/div/div[1]/div[2]/form/div/div[5]/button/span')

sign_in_button.click()

# --- Wait for greeting text (e.g., "Hi John") ---
greeting = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-automation-id="account-icon-button"]')))
greeting_text = greeting.text

# --- Validate text ---
assert "Hi John" in greeting_text, f"❌ Greeting text not found. Found: '{greeting_text}'"
print("✅ Login successful. Greeting found:", greeting_text)

# --- Screenshot for evidence ---
driver.save_screenshot("jcpenney_login_success.png")

driver.quit()
