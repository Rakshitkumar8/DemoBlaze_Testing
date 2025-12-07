from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------ CONFIG ------------
BASE_URL = "https://www.demoblaze.com/"
USERNAME = "your_username_here"      # put your real DemoBlaze username
PASSWORD = "your_password_here"      # put your real DemoBlaze password
# ---------------------------------

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# -------- VALID LOGIN TEST --------
driver.get(BASE_URL)

# Click "Log in"
login_link = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
login_link.click()

# Enter username
username_input = wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
username_input.clear()
username_input.send_keys(USERNAME)

# Enter password
password_input = driver.find_element(By.ID, "loginpassword")
password_input.clear()
password_input.send_keys(PASSWORD)

# Click "Log in" button
login_button = driver.find_element(By.XPATH, "//button[@onclick='logIn()']")
login_button.click()

# Verify "Welcome <username>" appears
welcome_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Welcome')]")))
if "Welcome" in welcome_link.text:
    print(" VALID LOGIN TEST PASSED:", welcome_link.text)
else:
    print(" VALID LOGIN TEST FAILED: Welcome text not found")

# Logout so we can test invalid login
logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout2")))
logout_link.click()

# -------- INVALID LOGIN TEST --------
# Open login modal again
login_link = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
login_link.click()

# Enter valid username and wrong password
username_input = wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
username_input.clear()
username_input.send_keys(USERNAME)

password_input = driver.find_element(By.ID, "loginpassword")
password_input.clear()
password_input.send_keys("WrongPassword123")

login_button = driver.find_element(By.XPATH, "//button[@onclick='logIn()']")
login_button.click()

# Wait for alert and read message
alert = wait.until(EC.alert_is_present())
alert_text = alert.text
print("Alert for invalid login:", alert_text)
alert.accept()

print(" INVALID LOGIN FLOW EXECUTED (alert appeared)")

driver.quit()
