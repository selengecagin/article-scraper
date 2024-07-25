import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Setup the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Navigate to Google Turkey
    driver.get("https://www.google.com.tr")

    # Wait for the page to load
    time.sleep(3)

    # Find the search box
    search_box = driver.find_element(By.NAME, "q")

    # Wait before typing
    time.sleep(2)

    # Type "Hello World!" in the search box
    search_box.send_keys("Hello World!")

    # Wait before pressing Enter
    time.sleep(2)

    # Press Enter to perform the search
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(5)

finally:
    # Close the browser after a short delay to see the result
    time.sleep(5)
    driver.quit()
