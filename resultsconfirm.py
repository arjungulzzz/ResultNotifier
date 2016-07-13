from selenium import webdriver
from selenium.webdriver.support.ui import Select
import ctypes
import requests
import urllib.request
import re
import os
import time
import subprocess
MessageBox=ctypes.windll.user32.MessageBoxW
driver=webdriver.Chrome('C:\\Users\\Arjun\\Downloads\\chromedriver.exe')
driver.get('http://duexam.du.ac.in/RSLT_MJ2016/Students/List_Of_Declared_Results.aspx')

select = Select(driver.find_element_by_name("ddlexamtype"))
select.select_by_visible_text("Semester")
select = Select(driver.find_element_by_name("ddlexamflag"))
select.select_by_visible_text("UG_SEMESTER_4Y")
driver.find_element_by_name('btnsearch').click()
driver.implicitly_wait(100)
if(driver.page_source.find('Computer Science')!=-1):
    subprocess.call(['python','resultssaver.py'])
else:
    MessageBox(None, 'LOL, JUST KIDDING', 'ROFL', 0)

driver.quit()


