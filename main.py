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


def login_sucessfully():
    ele = driver.find_element(By.ID, 'userid-inputEl')
    ele2 = driver.find_element(By.ID, 'textfield-1017-inputEl')
    ele3 = driver.find_element(By.ID, 'textfield-1019-inputEl')
    captcha = driver.find_element(By.ID, 'component-1011')
    captcha.screenshot('screenshot.png')
    Account = account.get()
    Password = password.get()
    ele.send_keys(Account)
    sleep(1)
    ele2.send_keys(Password)
    sleep(1)
    login_button = driver.find_element(
        By.XPATH, '/html/body/center/table/tbody/tr/td[2]/div/div/div[3]/div/div/div[1]')

    with open('screenshot.png', 'rb') as f:
        img = f.read()
    text = ocr.classification(img)
    text = text.lower()
    text = text.replace('\\', 'l')
    text = text.replace('十', '+')
    text = text.replace('0', 'o')
    white_list = 'abcdefghijklmnopqrstuvwxyz123456789+-'
    text = replace_chars_except_whitelist(text, white_list)

    print(text)
    ele3.send_keys(text)
    sleep(5)
    login_button.click()
    sleep(5)
    now_url = driver.current_url
    if now_url == 'https://cos1s.ntnu.edu.tw/AasEnrollStudent/IndexCtrl?language=TW':
        return True
    return False


def do_it():
    while True:
        if login_sucessfully() == True:
            break
        driver.refresh()
        sleep(10)
    driver.find_element(
        By.XPATH, '/html/body/center/table[1]/tbody/tr/td[1]/div/div/div[3]/div/div/div').click()
    sleep(2)
    Course_selection()


def END():
    driver.close()


def Course_selection():
    iframe = driver.find_element(By.XPATH, '//*[@id="stfseldListDo"]')
    driver.switch_to.frame(iframe)
    query_button = driver.find_element(
        By.XPATH, '//*[@id="query"]')
    query_button.click()
    sleep(2)
    driver.switch_to.default_content()
    iframe = driver.find_element(By.XPATH, '//*[@id="stfseldListDo"]')
    driver.switch_to.frame(iframe)
    search_column = driver.find_element(By.ID, 'serialNo-inputEl')
    search_button = driver.find_element(By.ID, 'button-1060-btnEl')
    search_column.send_keys('1009')
    search_button.click()


def logout():
    driver.find_element(By.ID, 'button-1017')


options = Options()
url = 'https://cos1s.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW'
options.path = "C:\\climbbug\\msedgedriver.exe"
ocr = ddddocr.DdddOcr()
driver = webdriver.Edge(options=options)
driver.get(url)
driver.maximize_window()
# GUI_DESIGN
window = tkinter.Tk()
window.title('NTNU_Rob_Course')
window.geometry('380x400')
window.resizable(False, False)
end_button = tkinter.Button(text='End', command=END)
start_button = tkinter.Button(text='Start', command=do_it)
end_button.place(x=100, y=300)
start_button.place(x=300, y=300)
account = tkinter.Entry()
password = tkinter.Entry(show='*')
Course_number = tkinter.Entry()
account.place(x=60, y=0)
password.place(x=60, y=20)
Course_number.place(x=60, y=40)
lb = tkinter.Label(text='帳號　　:')
lb2 = tkinter.Label(text='密碼　　:')
lb3 = tkinter.Label(text='課程代碼:')
lb.place(x=0, y=0)
lb2.place(x=0, y=20)
lb3.place(x=0, y=40)
window.iconbitmap('apfsg-43i9v-001.ico')

window.mainloop()
# https://cos1s.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW
# https://cos2s.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW
# https://cos3s.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW
# https://cos4s.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW
# https://cos5s.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW
# https://cos1s.ntnu.edu.tw/AasEnrollStudent/IndexCtrl?language=TW
