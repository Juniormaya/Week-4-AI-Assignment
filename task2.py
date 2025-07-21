# Pseudocode for Selenium + Python + AI plugin
from selenium import webdriver
from selenium.webdriver.common.by import By

def login_test(username, password):
    driver = webdriver.Chrome()
    driver.get("http://amaya.com/login")
    driver.find_element(By.ID, "nyamalo").send_keys(username)
    driver.find_element(By.ID, "plb55").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    # Wait for the page to load after login
    driver.implicitly_wait(5)
    # AI plugin auto-suggestion for visual verification or element checks
    try:
        driver.find_element(By.ID, "Logout-button")
        result = "Login successful"
    except:
        result = "Login failed"
    driver.quit()  # Clean up the driver after each test
    return result
    
# Run the login test
print(login_test("testuser", "testpassword"))  # Expected output: "Login successful"
print(login_test("wronguser", "wrongpassword"))  # Expected output: "Login failed"