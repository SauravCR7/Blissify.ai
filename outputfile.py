from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def getout(X,Y):
	#getting music 
	music,music_link = getmusic(Y)[0],getmusic(Y)[1]

	#getting poems
	poems = getpoem(X)

	#getting films
	films = getfilms(X)

	#opening output page
	driver = webdriver.Chrome()         
	driver.set_page_load_timeout(20)
	driver.get("file:///E:/new/index.html#")
	driver.maximize_window()
	driver.implicitly_wait(20)

