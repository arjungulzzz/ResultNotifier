from selenium import webdriver
from selenium.webdriver.support.ui import Select
import ctypes
import requests
import urllib.request
import re
import os
import time
import subprocess
from selenium.webdriver.common.keys import Keys
import pyautogui
import html5lib
from bs4 import BeautifulSoup
#StudentNames=['AANCHAL BANSAL','ABHINAV KUMAR','ADITYA KUMAR','AJAY KUMAR','AKHIL JUNEJA', 'AKSHAY KALIA', 'AMAN KUMAR', 'AMIT KUMAR', 'AMIT YADAV', 'ANJANA KUMARI', 'ANMOL AGNIHOTRI', 'ANMOL GUPTA', 'ANUJ KATIYAR', 'ANUJ KUMAR SAHU', 'ANURAG SHEKHAR', 'ARCHA JAIN', 'ARJUN GULYANI', 'ARPIT KUMAR', 'ARUSH VERMA', 'AYUSH JAIN', 'AYUSHI GUPTA', 'CHESHTA SONI','DEEPAK KUMAR', 'DEEPANSHU', 'DEV SALUJA', 'DEVANSHU TANEJA', 'DIPANSHU SHARMA', 'GANESH PRASAD', 'GAURAV KISHORE', 'GULSHAN KUMAR MEENA', 'HANIL KATHURIA', 'HARISH', 'HIMANI SETHI', 'HIMANSHI', 'KARTIKEY GOYAL', 'KONARK VERMA', 'KUNAL DARGAN', 'KUNWAR VIKRANT', 'MADHUR VASHISHT', 'MANISH CHANDRA', 'MANJEET YADAV', 'MEHUL SHARMA', 'MOHIT GANGWAR', 'MOHIT KUMAR', 'MUDIT AGGARWAL', 'NARESH KUSHMAKAR', 'NAYAN SHARMA', 'NEEL KUMAR', 'NIDHI SAKARWAL', 'NIDHI SHARMA','NIKHIL GUPTA']
SStudentNames=['AANCHAL BANSAL','ABHINAV KUMAR','ADITYA KUMAR','AJAY KUMAR','AKHIL JUNEJA', 'AKSHAY KALIA', 'AMAN KUMAR', 'AMIT KUMAR', 'AMIT YADAV', 'ANJANA KUMARI', 'ANMOL AGNIHOTRI', 'ANMOL GUPTA', 'ANUJ KATIYAR', 'ANUJ KUMAR SAHU', 'ANURAG SHEKHAR', 'ARCHA JAIN', 'ARJUN GULYANI', 'ARPIT KUMAR', 'ARUSH VERMA', 'AYUSH JAIN', 'AYUSHI GUPTA', 'CHESHTA SONI','DEEPAK KUMAR', 'DEEPANSHU', 'DEV SALUJA', 'DEVANSHU TANEJA', 'DIPANSHU SHARMA', 'GANESH PRASAD', 'GAURAV KISHORE', 'GULSHAN KUMAR MEENA', 'HANIL KATHURIA', 'HARISH', 'HIMANI SETHI', 'HIMANSHI', 'KARTIKEY GOYAL', 'KONARK VERMA','KUNWAR VIKRANT', 'MADHUR VASHISHT', 'MANISH CHANDRA', 'MANJEET YADAV', 'MEHUL SHARMA', 'MOHIT GANGWAR', 'MOHIT KUMAR', 'MUDIT AGGARWAL', 'NARESH KUSHMAKAR', 'NAYAN SHARMA', 'NEEL KUMAR', 'NIDHI SAKARWAL', 'NIDHI SHARMA','NIKHIL GUPTA']
StudentRoll=['4135441001','4135441002','4135441003','4135441004','4135441005','4135441006','4135441007','4135441008','4135441009','4135441010','4135441012','4135441013','4135441014','4135441015','4135441016','4135441017','4135441018','4135441019','4135441020','4135441021','4135441022','4135441023','4135441024','4135441025','4135441026','4135441027','4135441029','4135441030','4135441031','4135441032','4135441033','4135441035','4135441037','4135441038','4135441039','4135441040','4135441042','4135441043','4135441044','4135441045','4135441047','4135441049','4135441050','4135441051','4135441052','4135441053','4135441054','4135441055','4135441056','4135441058']
MessageBox=ctypes.windll.user32.MessageBoxW
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

count=0;
while (count<51):
    rollno = driver.find_element_by_name('txtrollno')
    rollno.click()
    rollno.send_keys(StudentRoll[count])
    name = driver.find_element_by_name('txtname')
    name.click()
    name.send_keys(StudentNames[count])
    driver.find_element_by_name('btnsearch').click()
    time.sleep(5)
    
    html=driver.page_source
    soup = BeautifulSoup(html)
    table=soup.find_all('table',id='gvrslt')
    fileObj=open(StudentNames[count]+'.txt','w')
    fileObj.write(str.join(u'\n', map(str,table)))
    fileObj.close()
    driver.back()
    rollno = driver.find_element_by_name('txtrollno')
    rollno.clear()
    name = driver.find_element_by_name('txtname')
    name.clear()
    count=count+1
    

    
    
#driver.get_screenshot_as_file('Arjun.jpeg')
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#MessageBox(None, 'Result Saved', 'hmm', 0)
#driver.quit()

