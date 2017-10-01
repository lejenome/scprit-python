from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json


browser = webdriver.PhantomJS("/home/firas/git/scripts-python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs",  service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
browser.set_window_size(1120, 550)

print(browser.current_url)
browser.get("https://youtube.com/feed/trending/")
time.sleep(10)
browser.maximize_window()
f = open('data.json', 'r+')
f.truncate()
top10 = browser.find_elements(By.XPATH, "//a[contains(@class, 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link ')]")
top10info = browser.find_elements(By.XPATH, "//ul[contains(@class, 'yt-lockup-meta-info')]")
file = open('youtube.txt','w') 
time.sleep(5)
k = 0 
for top in top10:
	ch =''
	info = top10info[k].find_elements_by_tag_name("li")
	t = top.get_attribute("title")
	ch = ch + t
	print("title = ",t)
	for i in info:
		texte = i.text
		ch = ch + "\n" + texte
		print(texte)
		data = { 'title' : t , 'date' : texte , 'vue' : texte } 
	json_str = json.dumps(data)
	with open('data.json', 'a') as f:
		json.dump(data, f)
	k = k + 1
	file.write(ch)
