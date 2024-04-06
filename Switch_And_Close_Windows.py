from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# initialize chrome webdriver
driver = webdriver.Chrome()

#open cowin
driver.get("https://www.cowin.gov.in/")

parent_handle = driver.current_window_handle

print("Homepage window id: ", parent_handle)

faq_button = driver.find_element(By.LINK_TEXT, "FAQ")
faq_button.click()

print("FAQ window id: ", driver.window_handles[1])

partner_button = driver.find_element(By.LINK_TEXT, "PARTNERS")
partner_button.click()
print("Partner window id: ", driver.window_handles[2])

#get all handles
window_handles = driver.window_handles

# Iterate over the window handles
for window_handle in window_handles:
    # Close all child windows (window handles) except homepage (parent handle)
    if window_handle != parent_handle:
        driver.switch_to.window(window_handle)
        driver.close()

time.sleep(15)


