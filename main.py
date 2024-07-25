import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Setup the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Navigate to "https://code-maze.com/"
    driver.get("https://code-maze.com/latest-posts-on-code-maze/")

    # Wait 2 seconds
    time.sleep(2)

    # Find <h2> elements with class "entry-title"
    titles = driver.find_elements(By.CSS_SELECTOR, "h2.entry-title")

    # Initialize a list to hold the data
    data = []

    # get the href value of the first <a> element in the <h2> element
    for title in titles:
        title_text = title.find_element(By.CSS_SELECTOR, "a").text
        link = title.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

        # Print the text and href
        print(title_text)
        print(link)

        # Append the title and link to the data list
        data.append({"title": title_text, "link": link})

    # Save the titles and links to a json file
    with open("titles.json", "w") as f:
        json.dump(data, f, indent=4)

    # Wait 2 seconds
    time.sleep(2)

finally:
    # Close the browser after a short delay to see the result
    time.sleep(5)
    driver

