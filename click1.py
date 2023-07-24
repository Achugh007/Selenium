import selenium
import time

driver = selenium.webdriver.Chrome()

driver.get("file:///ClickMe.html")

button = driver.find_element_by_xpath("//button[@id='clickMe']")

button.click()

time.sleep(2)

assert driver.find_element_by_xpath("//p[@id='output']").text == "You clicked the button!"

driver.quit()