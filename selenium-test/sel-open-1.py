# myke tests selenium
# 2019-04-12 v.0.2

# YouTube Video: https://www.youtube.com/watch?v=eDrFWRi13DY

from selenium import webdriver

# Old way of doing things that should work with Firefox, but soesn.t
# ~ driver = webdriver.Firefox()
# ~ driver.get("http://google.com")

# Another way of doing things that should work with Chrome, but doesn't'
chromedriver = "chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://google.com")

#site = r"http://www.myke.spb.ru"

#chromedriver = "chromedriver"
#driver = webdriver.Chrome(chromedriver)
#driver.get(site)
