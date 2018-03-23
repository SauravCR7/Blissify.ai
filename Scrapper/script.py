# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 21:58:30 2018

@author: Utkarsh
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()