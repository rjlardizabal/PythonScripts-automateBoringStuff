#!/usr/bin/python3


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()

browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('body')

while True:
    htmlElem.send_keys(Keys.ARROW_UP)
    htmlElem.send_keys(Keys.ARROW_RIGHT)
    htmlElem.send_keys(Keys.ARROW_DOWN)
    htmlElem.send_keys(Keys.ARROW_LEFT)
