#This is a script checks for Result of 3 sem every 15 Min 
#Author Aagam Shah
#Just for Fun
import ctypes
import requests
import urllib.request
import re
import os
import time
MessageBox=ctypes.windll.user32.MessageBoxW 
while 1:
 
    with urllib.request.urlopen('http://duexam.du.ac.in/RSLT_MJ2016/Students/List_Of_Declared_Results.aspx') as response:
        html=response.read()

    matches = html.find(b'Computer')  
 
 
    if matches == -1:
        MessageBox(None, 'Results not declared yet', 'Yeah', 0)
       #os.system("notify-send 'Yeah' 'Result is not declared yet'")
        time.sleep(5)
 
    #else:
       #os.system("notify-send 'Oops' 'Result Declared'")
       #quit()
