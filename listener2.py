import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigating to:", url)

    def after_navigate_to(self, url, driver):
        print("After navigating to:", url)

    def before_navigate_back(self, driver):
        print("Before navigating back", driver.current_url)

    def after_navigate_back(self, driver):
        print("After navigating back", driver.current_url)

    def before_navigate_forward(self, driver):
        print("Before navigating forward", driver.current_url)

    def after_navigate_forward(self, driver):
        print("After navigating forward", driver.current_url)

    def before_find(self, by, value, driver):
        print("Before find")

    def after_find(self, by, value, driver):
        print("After find")

    def before_click(self, element, driver):
        print("Before click")

    def after_click(self, element, driver):
        print("After click")

    def before_change_value_of(self, element, driver):
        print("Before change value of")

    def after_change_value_of(self, element, driver):
        print("After change value of")

    def before_execute_script(self, script, driver):
        print("Before execute script")

    def after_execute_script(self, script, driver):
        print("After execute script")

    def before_quit(self, driver):
        print("Before quit")

    def after_quit(self, driver):
        print("After quit")

    def on_exception(self, exception, driver):
        print("On exception")

class Test(unittest.TestCase):
    def test_logging_file(self):
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=option)
        edriver = EventFiringWebDriver(driver, CustomListener())

        try:
            edriver.get("http://localhost:1180/test.html")

            # Wait for the input field to be located and become visible
            input_field = WebDriverWait(edriver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input'))
            )
            input_field.send_keys("Event")

            # Wait for the button to be located and become clickable
            button = WebDriverWait(edriver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input'))
            )
            button.click()

        except Exception as e:
            print(e)
