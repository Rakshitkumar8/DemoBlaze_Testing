from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------ CONFIG ------------
BASE_URL = "https://www.demoblaze.com/"
USERNAME = "your_username_here"
PASSWORD = "your_password_here"
PRODUCT_NAME = "Samsung galaxy s6"
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

# -------- ADD PRODUCT TO CART --------
product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, PRODUCT_NAME)))
product_link.click()

add_to_cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart")))
add_to_cart_link.click()

alert = wait.until(EC.alert_is_present())
print("Alert after Add to cart:", alert.text)
alert.accept()

# Go to Cart
cart_link = wait.until(EC.element_to_be_clickable((By.ID, "cartur")))
cart_link.click()

# Optional: verify product is in cart
product_in_cart = wait.until(EC.visibility_of_element_located((By.XPATH, f"//td[text()='{PRODUCT_NAME}']")))
print("Product in cart:", product_in_cart.text)

# -------- PLACE ORDER --------
place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
place_order_button.click()

# Fill form fields
name_input = wait.until(EC.visibility_of_element_located((By.ID, "name")))
name_input.send_keys("Test User")

country_input = driver.find_element(By.ID, "country")
country_input.send_keys("India")

city_input = driver.find_element(By.ID, "city")
city_input.send_keys("Bangalore")

card_input = driver.find_element(By.ID, "card")
card_input.send_keys("4111111111111111")

month_input = driver.find_element(By.ID, "month")
month_input.send_keys("12")

year_input = driver.find_element(By.ID, "year")
year_input.send_keys("2028")

purchase_button = driver.find_element(By.XPATH, "//button[text()='Purchase']")
purchase_button.click()

# -------- VERIFY SUCCESS MESSAGE --------
success_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2")))
print("Success popup title:", success_header.text)

if "Thank you" in success_header.text:
    print("✅ PLACE ORDER TEST PASSED")
else:
    print("❌ PLACE ORDER TEST FAILED – Success message not found")

driver.quit()
