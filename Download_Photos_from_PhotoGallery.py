# Download
import os
import urllib.request

import self
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

print("Downloading starts")
driver = webdriver.Chrome()

print("Extracting pictures from the webpage")
driver.get('https://labour.gov.in/photo-gallery/')
images = driver.find_elements(By.TAG_NAME,'img')
image_folder = "C:\\Users\\admin\\Desktop\\Task21"

# Validate whether folder is present on given path or not. If not then create the folder.
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Counter
i = 1

# Download only 10 images from the media webpage
print("Saving pictures from the webpage to the directory")
for image in images:
    src = image.get_attribute('src')
    if i < 11:
        urllib.request.urlretrieve(src, os.path.join(image_folder, "myimage" + str(i) + ".jpg"))
    i = i+1
print("Pictures downloaded successfully")