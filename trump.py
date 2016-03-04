# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

import time

wd = WebDriver()
wd.set_window_size(1280, 1000)
wd.implicitly_wait(15)

def wait(s):
    time.sleep(s)

try:
    wd.get("http://trumpdonald.org/")

    while True:
        wd.find_element_by_id("can").click()
finally:
    raise Exception("Test exited.")

wd.quit()
