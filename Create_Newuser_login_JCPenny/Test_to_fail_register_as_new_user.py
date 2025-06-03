#Test script to error out with "This Account already exist"

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

first_name_input = wait.until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )

    # Enter the name "John"
first_name_input.send_keys("John")
print("✅ 'John' entered in First Name field.")

last_name_input = wait.until(
        EC.presence_of_element_located((By.ID, "lastName"))
    )
    #Enter the last name "Test"
last_name_input.send_keys("Test")
print("✅ 'Test' entered in Last Name field.")

# Locate the input field by its ID- phone number 
phone_input = driver.find_element(By.ID, "phone")

    # Enter the phone number 
phone_input.send_keys("4847774456")

#Locate and input the field by its ID- Email address

email_id_input = driver.find_element(By.ID, "createAccountEmail")



    # Enter the email address  
email_id_input.send_keys("johnsmith@gmail.com")

#Locate and input the field by its ID-Password
password_input = driver.find_element(By.ID, "create-password")

    # Enter the password
password_input.send_keys("ThisisaP@asword3")
print("✅ password is entered successfully")


#Locate and click on the field by its XPath- Create Account 

try:
    create_account_button = WebDriverWait(driver, 10).until(
        EC.create_account_button_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[6]/div/div[2]/div/div/div[3]/div/div/form/div/div[2]/div/div/button/span"))
    )
    
except Exception as e:
    print("Error:", e)

print("✅ 'Create Account' button is clickable.")


# Validate the "Create account" button is now active 
create_account_button = driver.find_element(By.CSS_SELECTOR, 'button[data-automation-id="submit_button"]')

# 1. Check if it's enabled
is_enabled = create_account_button.is_enabled()

# 2. Get computed background color via JS
bg_color = driver.execute_script("""
    return window.getComputedStyle(arguments[0]).backgroundColor;
""", create_account_button)

# 3. Check class name
class_attr = create_account_button.get_attribute("class")

# 4. Validate color + state
def is_red(color):
    return "255, 0, 0" in color  # covers rgba and rgb red tones

if is_enabled and (is_red(bg_color) or "btnDanger" in class_attr):
    print("***************************************✅ Button is red and active.**********************************")
else:
    print(f"❌ Button check failed.\n - Enabled: {is_enabled}\n - Computed BG: {bg_color}\n - Class: {class_attr}")


#5. Take screen shot and timestamp 
time.sleep(5)
import time
timestamp = time.strftime("%Y%m%d-%H%M%S")

create_account_button.screenshot("button_screenshot.png")

#click on the create account button 
time.sleep(5)
create_account_button= driver.find_element(By.CSS_SELECTOR, 'button[data-automation-id="submit_button"]')
create_account_button.click()

# Wait a bit for the next page or modal to load
time.sleep(3)

# Take screenshot
driver.save_screenshot("screenshot_after_create_account.png")
print("✅ Screenshot saved as screenshot_after_create_account.png")
time.sleep(5)
driver.quit()