import selenium
import time

driver = webdriver.Chrome("executable_path="C://Selenium_Libraries//chromedriver_win32//chromedriver.exe")

try:
    driver.get("file:///c://Users/admin/Desktop//ClickMe.html")
    time.sleep(5)
    driver.execute_script('return document.getElementById("button").click()')

    print("Test passed!")

except Exception as e:
    print("Test Failed")

driver.quit()