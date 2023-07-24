from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver with the correct path to ChromeDriver
chrome_driver_path = "C:/path/to/chromedriver.exe"  # Replace with the actual path to chromedriver.exe
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigate to the ClickMe.html file on the desktop
file_path = "file:///C:/Users/{YourUsername}/Desktop/ClickMe.html"  # Replace {YourUsername} with your Windows username
driver.get(file_path)

# Find the "Click Me!" button element
button = driver.find_element(By.TAG_NAME, "button")

# Click the button
button.click()

# Get the text from the alert dialog
alert_text = driver.switch_to.alert.text

# Verify JavaScript execution
expected_text = "Hello User! Welcome!"
if alert_text == expected_text:
    print("Test Passed! JavaScript code executed successfully.")
else:
    print("Test Failed! JavaScript code execution did not produce the expected result.")

# Close the WebDriver
driver.quit()
