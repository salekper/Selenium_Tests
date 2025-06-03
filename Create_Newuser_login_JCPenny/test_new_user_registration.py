# updated script to use a new random "email address" for each registration. This resolves the issue reported in https://github.com/salekper/Selenium_Tests/issues/1

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import undetected_chromedriver as uc
import random
import string

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

try:

    sign_up_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-automation-id="signup_button"]'))
    )

    # Click the button
    sign_up_button.click()
    print("✅ Clicked 'Sign Up Now' button successfully.")

except Exception as e:
    print("❌ Error:", e)
time.sleep(2)

# === Generate random email ===
def generate_random_email():
    prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{prefix}@gmail.com"

# === Step 3: Begin account creation ===
try:
    

    wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys("John")
    wait.until(EC.presence_of_element_located((By.ID, "lastName"))).send_keys("Test")
    driver.find_element(By.ID, "phone").send_keys("4847774456")

    # Use generated email
    random_email = generate_random_email()
    driver.find_element(By.ID, "createAccountEmail").send_keys(random_email)
    print(f"✅ Using email: {random_email}")
    driver.find_element(By.ID, "create-password").send_keys("ThisisaP@asword3")
    print("✅ Form filled.")

    create_btn = driver.find_element(By.CSS_SELECTOR, 'button[data-automation-id="submit_button"]')
    is_enabled = create_btn.is_enabled()
    bg_color = driver.execute_script("return window.getComputedStyle(arguments[0]).backgroundColor;", create_btn)
    class_attr = create_btn.get_attribute("class")

    def is_red(color):
        return "255, 0, 0" in color

    if is_enabled and (is_red(bg_color) or "btnDanger" in class_attr):
        print("✅ Button is red and active.")
    else:
        print("❌ Button check failed.")

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    create_btn.screenshot(f"button_{timestamp}.png")

    create_btn.click()
    time.sleep(3)
    driver.save_screenshot(f"post_submit_{timestamp}.png")
    print("✅ Account created. Screenshot saved.")

except Exception as e:
    print("❌ Test failed:", e)

# === Cleanup ===
driver.quit()
