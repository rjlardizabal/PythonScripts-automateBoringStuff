#! python 3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('body')

while True:
    htmlElem.send_keys(Keys.ARROW_UP)
    time.sleep(.01)
    htmlElem.send_keys(Keys.ARROW_RIGHT)
    time.sleep(.01)
    htmlElem.send_keys(Keys.ARROW_DOWN)
    time.sleep(.01)
    htmlElem.send_keys(Keys.ARROW_LEFT)
    time.sleep(.01)
