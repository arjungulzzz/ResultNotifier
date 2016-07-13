#This is a script checks for Result of 6 sem every 600 Seconds 
#Author Arjun Gulyani
#Just for Fun

import subprocess
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

    matches = html.find(b'37')  
 
 
    if matches != -1:
        MessageBox(None, 'RESULT NOT OUT YET', 'YEAH!!', 0)
        time.sleep(600)
 
    else:
        subprocess.call(['python','resultsconfirm.py'])
