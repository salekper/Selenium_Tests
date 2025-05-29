from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

# Initialize WebDriver
driver = webdriver.Chrome()  # or webdriver.Chrome(service=service, options=chrome_options)

# Open bcwsa website
driver.get("https://www.bcwsa.net/")

# Optional: keep the browser open for a while
time.sleep(2)  # Keeps the browser open for 2 seconds

try:
    button = driver.find_element(By.XPATH, "//a[contains(@class, 'elementor-button-link') and contains(., 'Pay Your Bill')]")
    button.click()
except Exception as e:
    print("Could not find 'Pay Your Bill':", e)



# Get all window handles
tabs = driver.window_handles

# Switch to the newest tab
driver.switch_to.window(tabs[-1])

# Keep browser open for 2 seconds to view the result
time.sleep(2)
try:
    # Locate the <span> using the absolute XPath
    span = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/ul/li[1]/a/span")

    # Click the parent <a> tag using JavaScript
    link = span.find_element(By.XPATH, "..")
    driver.execute_script("arguments[0].click();", link)

    print("Clicked successfully.")

except Exception as e:
    print("Error:", e)

try:
    # Find the "Update Your Customer Contact Information" button
    button = driver.find_element(By.XPATH, "//a[span/span[text()='Update Your Customer Contact Information']]")

    # Scroll to the button
    driver.execute_script("arguments[0].scrollIntoView(true);", button)

    # Click using JavaScript (more reliable)
    driver.execute_script("arguments[0].click();", button)

    print("Button clicked successfully.")

except Exception as e:
    print("Error:", e)
# Get all window handles
tabs = driver.window_handles

# Switch to the newest tab
driver.switch_to.window(tabs[-1])

# Locate the input field by its ID
first_name_input = driver.find_element(By.ID, "input_9_2_3")

    # Enter the name
first_name_input.send_keys("John")


# Locate the last name input field by its ID
last_name_input = driver.find_element(By.ID, "input_9_2_6")

# Enter the last name
last_name_input.send_keys("Doe")
time.sleep(2)

# Enter the Account number
Account_number_input = driver.find_element(By.ID, "input_9_6")
Account_number_input.send_keys("145644866")
time.sleep(2)

# Enter the phone number
phone_number_input = driver.find_element(By.ID, "input_9_9")
phone_number_input.send_keys("4446662276")
time.sleep(2)


#Click on Home radio button
phone_type = driver.find_element(By.ID, "choice_9_10_1")
phone_type.click()
time.sleep(2)

# Enter the cell phone number
cell_number_input = driver.find_element(By.ID, "input_9_4")
cell_number_input.click()
cell_number_input.send_keys("4446662200")
time.sleep(5)

# Enter the email address
email_address_input = driver.find_element(By.ID, "input_9_3")
email_address_input.send_keys("John_Doe@gmail.com")
time.sleep(2)

#Click Submit on the form

from selenium.webdriver.common.by import By

element = driver.find_element(By.ID, "gform_submit_button_9")

# Scroll to the element using JavaScript
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

# Optional: pause for a moment to ensure scroll completes
import time
time.sleep(1)

# Now you can click or interact with it
element.click()
print("**************************************TEST WAS A SUCCESS**************************.")
driver.quit
