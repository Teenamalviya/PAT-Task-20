import time
from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "C:\\Users\\admin\\Desktop"}
options.add_experimental_option("perfs", prefs)

# initialize chrome
driver = webdriver.Chrome()

# get url
driver.get("https://labour.gov.in/monthly-progress-report")

# Open monthly report page
download_button = driver.find_element(By.LINK_TEXT,'Download(221.53 KB)')
download_button.click()

# Accept the pop-up alert message to begin download
driver.switch_to.alert.accept()
time.sleep(15)

# Close the browser
driver.quit()