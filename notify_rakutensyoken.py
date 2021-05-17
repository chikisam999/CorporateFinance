import time
import slackweb
from selenium import webdriver
import datetime
import pyautogui
import keyring
import os
import requests


ID = 'hogehoge'
password = 'hogehoge'

url = "https://notify-api.line.me/api/notify"
access_token = 'hogehoge'
headers = {'Authorization': 'Bearer ' + access_token}

today_name = datetime.datetime.now()
today_name2 = datetime.datetime.today()
filename = 'shot_{0:%Y%m%d}.png'.format(today_name)

driver = webdriver.Chrome()
driver.get('https://www.rakuten-sec.co.jp/')
driver.get('https://www.rakuten-sec.co.jp/ITS/V_ACT_Login.html')
elem_username = driver.find_element_by_id('form-login-id')
elem_username.send_keys(ID)
elem_password = driver.find_element_by_id('form-login-pass')
elem_password.send_keys(password)
pyautogui.press('enter')
driver.set_window_size(1050, 800) 
driver.save_screenshot(filename)


"""
asset = driver.find_element_by_id("asset_total_asset")
diff = driver.find_element_by_id("asset_total_asset_diff")
"""

message = ('楽天証券' + str(datetime.datetime.now().date()))
image = 'test.png'
payload = {'message': message}
files = {'imageFile': open(filename, 'rb')}
r = requests.post(url, headers=headers, params=payload,files=files)
