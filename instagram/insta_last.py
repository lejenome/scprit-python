from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('http://instagram.com')

time.sleep(10)

phone_email = browser.find_element_by_name('emailOrPhone')
phone_email.clear()
phone_email.send_keys('mohsenijkel@gmail.com')

full_name = browser.find_element_by_name('fullName')
full_name.clear()
full_name.send_keys('mohsenrt')

user_name = browser.find_element_by_name('username')
user_name.clear()
user_name.send_keys('mohseniju8547')

password_el = browser.find_element_by_name('password')
password_el.clear()
password_el.send_keys('azertycom')

password_el.send_keys(Keys.RETURN)

time.sleep(10)

browser.find_element_by_xpath("//a[contains(@class, '_8scx2 _gvoze coreSpriteDesktopNavProfile')]").click()

time.sleep(10)

browser.find_element_by_xpath("//a[contains(@class, '_t98z6')]").click()

time.sleep(10)

followers = browser.find_element_by_xpath("//a[contains(@class, '_2g7d5 notranslate _o5iw8')]")
last_follow = followers.get_attribute("title")
print(last_follow)


