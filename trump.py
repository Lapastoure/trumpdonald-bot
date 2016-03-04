# -*- coding: utf-8 -*-
import multiprocessing
import subprocess
import time
import sys

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

def wait(s):
    time.sleep(s)

def work(pid):
    print('Starting %s' % str(pid))
    wd = WebDriver()
    wd.set_window_size(1280, 1000)
    wd.implicitly_wait(15)

    try:
        wd.get("http://trumpdonald.org/")

        while True:
            wd.find_element_by_id("can").click()
    finally:
        raise Exception("Test exited. pid=%s" % str(pid))

    wd.quit()
    return None


if __name__ == '__main__':
    count = multiprocessing.cpu_count()
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    print(count)
    pool = multiprocessing.Pool(processes=count)
    print pool.map(work, range(0, count))
