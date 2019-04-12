# myke tests selenium
# 2019-04-12 v.1.0

# YouTube Video: https://www.youtube.com/watch?v=eDrFWRi13DY

from selenium import webdriver
# ~ options = webdriver.ChromeOptions()

# Old way of doing things that should work with Firefox, but soesn.t
# ~ driver = webdriver.Firefox()
# ~ driver.get("http://google.com")

# Another way of doing things that should work with Chrome, but doesn't'
#chromedriver = "chromedriver"
#driver = webdriver.Chrome(chromedriver)
#driver = webdriver.Chrome()

mysite = r"https://google.com"
driver = webdriver.Chrome()

# ~ driver = webdriver.Remote(site, webdriver.DesiredCapabilities.HTMLUNIT.copy())

driver.get(mysite)

#site = r"http://www.myke.spb.ru"

#chromedriver = "chromedriver"
#driver = webdriver.Chrome(chromedriver)
#driver.get(site)
