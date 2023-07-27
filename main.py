from selenium import webdriver
from selenium.webdriver.edge.options import Options
from PIL import Image
from selenium.webdriver.common.by import By
from io import BytesIO
import numpy as np
import cv2
import ddddocr
from time import sleep

options = Options()
url = 'https://cos1s.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW'
options.path = "C:\\climbbug\\msedgedriver.exe"
ocr = ddddocr.DdddOcr()
driver = webdriver.Edge(options=options)
driver.maximize_window()
driver.get("https://cos1s.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW")
sleep(3)
ele = driver.find_element(By.ID, 'userid-inputEl')
ele2 = driver.find_element(By.ID, 'textfield-1017-inputEl')
ele3 = driver.find_element(By.ID, 'textfield-1019-inputEl')
captcha = driver.find_element(By.ID, 'component-1011')
loc = captcha.location
size = captcha.size
left = loc['x']
top = loc['y']
right = loc['x'] + size['width']
bottom = loc['y'] + size['height']
screenshot = driver.get_screenshot_as_png()
screenshot = Image.open(BytesIO(screenshot))
screenshot.save("screenshot.png")
screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
region_screenshot = screenshot_cv[top:bottom, left:right]
region_screenshot_pil = Image.fromarray(
    cv2.cvtColor(region_screenshot, cv2.COLOR_BGR2RGB))
region_screenshot_pil.save("screenshot.png")
ele.send_keys('')
sleep(1)
ele2.send_keys('')
sleep(1)

with open('screenshot.png', 'rb') as f:
    img = f.read()
text = ocr.classification(img)
print(text)
sleep(5)
ele3.send_keys(text)
sleep(20)
driver.close()
