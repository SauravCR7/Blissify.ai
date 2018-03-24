# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 21:58:30 2018

@author: Utkarsh
"""

def getMusic(percent):
    if(percent < -20):
        strr = "blues"
    elif(percent > -20 and percent < 20):
        strr = "classical"
    else:
        strr = "alt-rock"
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
    
    #for Firefox
    driver = webdriver.Firefox()
    #for Chrome
    #driver = webdriver.Chrome()
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
    driver.implicitly_wait(50)
    #driver.close()
    names1 = driver.find_elements_by_class_name("title")
    names = []
    for name in names1:
        names.append(name.text)
    
    links = []
    
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        if(elem.get_attribute("href").startswith('https://www.youtube.com')):
            links.append(elem.get_attribute("href"))
    driver.close()

    k = {'x':names,'y':links}
    return k
#fix this call. Edit the integer to be passed and select genre based on mood
tup = getMusic(40)
print(tup)