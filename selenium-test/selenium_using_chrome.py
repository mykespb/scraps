# myke tests selenium
# 2019-04-12 v.0.1

# YouTube Video: https://www.youtube.com/watch?v=eDrFWRi13DY

from selenium import webdriver

# Old way of doing things that works with Firefox
# driver = webdriver.Firefox()
# driver.get("http:google.com")

site = r"http://www.myke.spb.ru"

chromedriver = "chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get(site)

