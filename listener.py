from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

class CustomListener(AbstractEventListener):
    def before_click(self, element, driver):
        print(f"Before clicking: {element.text}")

    def after_click(self, element, driver):
        print(f"After clicking: {element.text}")

# Create a new instance of the WebDriver
driver = webdriver.Chrome()

# Wrap the WebDriver with EventFiringWebDriver and attach the CustomListener
event_driver = EventFiringWebDriver(driver, CustomListener())

# Navigate to the test webpage
event_driver.get("https://www.example.com")  # Replace with the URL of the test webpage

# Find the elements and perform the click event
element1 = event_driver.find_element(By.XPATH, "//button[@id='button1']")
element1.click()

element2 = event_driver.find_element(By.XPATH, "//a[@class='link']")
element2.click()

# Close the WebDriver
event_driver.quit()
