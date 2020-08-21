# SELENIUM
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Opens the website
driver.get("https://www.amazon.co.uk/")

# Types it into the search bar then presses enter
link = driver.find_element_by_name("field-keywords")
link.send_keys("Marcus Aurelius - Meditations", Keys.RETURN)

# Prints out the text
main = driver.find_element_by_id("search")
print(main.text)

time.sleep(5)

driver.quit()

