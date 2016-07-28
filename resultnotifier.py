from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import subprocess
import ctypes
import requests
import urllib.request
import re
import os
import time
MessageBox=ctypes.windll.user32.MessageBoxW
req = Request("http://duexam.du.ac.in/RSLT_MJ2016/Students/List_Of_Declared_Results.aspx")

while 1:
    try:
        response = urlopen(req)
    except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            localtime=time.asctime(time.localtime(time.time()))
            print('at time --> ',localtime)
            time.sleep(100)
    except URLError as e:
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
                localtime=time.asctime(time.localtime(time.time()))
                print('at time --> ',localtime)
                time.sleep(100)
    else:
        while 1:
            try:
                with urllib.request.urlopen('http://duexam.du.ac.in/RSLT_MJ2016/Students/List_Of_Declared_Results.aspx') as response:
                    html=response.read()
                matches = html.find(b'39')
                if matches != -1:
                    MessageBox(None, 'RESULT NOT OUT YET', 'YEAH!!', 0)
                    time.sleep(600)
                else:
                    subprocess.call(['python','resultsconfirm.py'])
            except:
                time.sleep(20)
            else:
                break
                    
                        

        



       
