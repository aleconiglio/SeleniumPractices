from selenium import webdriver
from selenium.webdriver.common.by import By

driver =  webdriver.Chrome(executable_path="C:/chromedriver.exe")

driver.get()

cur_title = driver.title
expected_title = ""

if cur_title != expected_title:
    raise Exception("Se ingreso a ____ pero el título es {}".format(cur_title))

cur_url = driver.current_url
expected_url = ""
assert cur_url == expected_url, f"Clicked on _____ but the url opened was {cur_url}"
print(PASS)


