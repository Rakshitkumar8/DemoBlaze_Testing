from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------ CONFIG ------------
BASE_URL = "https://www.demoblaze.com/"
USERNAME = "your_username_here"         # same user as above
PASSWORD = "your_password_here"
PRODUCT_NAME = "Samsung galaxy s6"      # or any product name shown on homepage
# ---------------------------------

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# -------- LOGIN --------
driver.get(BASE_URL)

login_link = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
login_link.click()

username_input = wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
username_input.clear()
username_input.send_keys(USERNAME)

password_input = driver.find_element(By.ID, "loginpassword")
password_input.clear()
password_input.send_keys(PASSWORD)

login_button = driver.find_element(By.XPATH, "//button[@onclick='logIn()']")
login_button.click()

welcome_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Welcome')]")))
print("Logged in as:", welcome_link.text)

# -------- OPEN PRODUCT & ADD TO CART --------
# Click product link on home page
product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, PRODUCT_NAME)))
product_link.click()

# Click "Add to cart"
add_to_cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart")))
add_to_cart_link.click()

# Handle alert
alert = wait.until(EC.alert_is_present())
alert_text = alert.text
print("Alert after Add to cart:", alert_text)
alert.accept()

# -------- OPEN CART & VERIFY PRODUCT --------
cart_link = wait.until(EC.element_to_be_clickable((By.ID, "cartur")))
cart_link.click()

# Verify product name present in cart table
product_in_cart = wait.until(EC.visibility_of_element_located((By.XPATH, f"//td[text()='{PRODUCT_NAME}']")))

if product_in_cart is not None:
    print("✅ ADD TO CART TEST PASSED – Product found in cart:", product_in_cart.text)
else:
    print("❌ ADD TO CART TEST FAILED – Product not found in cart")

driver.quit()
