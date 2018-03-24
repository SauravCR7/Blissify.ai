# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 21:58:30 2018

@author: Utkarsh
"""

def getMusic(percent):
    strr = "blues"
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
    
    driver = webdriver.Firefox()
    driver.get("https://moodfuse.com/")
    select = Select(driver.find_element_by_name("genre"))
    select.select_by_visible_text(strr)
    
    slidebar = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[2]/div[2]/input')
    height = slidebar.size['height']
    width = slidebar.size['width']

    from selenium.webdriver.common.action_chains import ActionChains
    move = ActionChains(driver);
    if width > height:
        move.click_and_hold(slidebar).move_by_offset(percent * width / 100, 0).release().perform()
    else:
       move.click_and_hold(slidebar).move_by_offset(percent * height / 100, 0).release().perform()

    #driver.switch_to_default_content()
    
    slidebar = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[3]/div[2]/input')
    height = slidebar.size['height']
    width = slidebar.size['width']

    move = ActionChains(driver);
    if width > height:
        move.click_and_hold(slidebar).move_by_offset(percent * width / 100, 0).release().perform()
    else:
       move.click_and_hold(slidebar).move_by_offset(percent * height / 100, 0).release().perform()
    
    slidebar = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[4]/div[2]/input')
    height = slidebar.size['height']
    width = slidebar.size['width']

    move = ActionChains(driver);
    if width > height:
        move.click_and_hold(slidebar).move_by_offset(percent * width / 100, 0).release().perform()
    else:
       move.click_and_hold(slidebar).move_by_offset(percent * height / 100, 0).release().perform()
    
    btn = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[5]/button')
    btn.click()
    #driver.close()
    names = driver.find_elements_by_class_name("title")
    if(names is not None):
        print("Got it")
    else:
        print("Didn't")
    for name in names:
        print(name.text)
    #print(names)
    links = driver.find_elements_by_class_name("links")
    if(links is not None):
        print("Got it")
    else:
        print("Didn't")
    for t in t_links:
        print (t.text)
      

#fix this call. Edit the integer to be passed and select genre based on mood
getMusic(-40)

#for 
    en1 = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[1]')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    