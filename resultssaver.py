from selenium import webdriver
from selenium.webdriver.support.ui import Select
import ctypes
import requests
import urllib.request
import re
import os
import time
import subprocess

driver=webdriver.Chrome('C:\\Users\\Arjun\\Downloads\\chromedriver.exe')
driver.get('http://duexam.du.ac.in/RSLT_MJ2016/Students/Combine_GradeCard.aspx')
select = Select(driver.find_element_by_name('ddlcollege'))
select.select_by_visible_text('Keshav Mahavidyalaya-(035)')
select = Select(driver.find_element_by_name('ddlexamtype'))
select.select_by_visible_text('Semester')
select = Select(driver.find_element_by_name('ddlexamflag'))
select.select_by_visible_text('UG_SEMESTER_4Y')
select = Select(driver.find_element_by_name('ddlstream'))
select.select_by_visible_text('Science')
select = Select(driver.find_element_by_name('ddlcourse'))
select.select_by_visible_text('(U.G)(FYUP)-B.Tech. Computer Science-(441)')
select = Select(driver.find_element_by_name('ddlpart'))
select.select_by_visible_text('III')
select = Select(driver.find_element_by_name('ddlsem'))
select.select_by_visible_text('VI')
rollno = driver.find_element_by_name('txtrollno')
rollno.click()
rollno.send_keys('4135441018')
name = driver.find_element_by_name('txtname')
name.click()
name.send_keys('Arjun Gulyani')
#driver.get_screenshot_as_file('Arjun.jpeg')
driver.find_element_by_name('btnsearch').click()
