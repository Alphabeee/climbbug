from selenium import webdriver
from selenium.webdriver.edge.options import Options
from PIL import Image
from selenium.webdriver.common.by import By
from io import BytesIO
import numpy as np
import cv2
import ddddocr
from time import sleep
import tkinter


def replace_chars_except_whitelist(input_string, whitelist, replacement=""):
    result = ""
    for char in input_string:
        if char in whitelist:
            result += char
        else:
            result += replacement
    return result


def do_it():
    driver.get(url)
    driver.maximize_window()
    sleep(3)
    driver.close()


options = Options()
url = 'https://cos1s.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW'
options.path = "C:\\climbbug\\msedgedriver.exe"
ocr = ddddocr.DdddOcr()

for i in range(10):
    driver = webdriver.Edge(options=options)
    do_it()
