#!/usr/bin/python3
from threading import Thread
import requests
from termcolor import colored
import sys

print(colored("\n--------------------------------","blue"))
print(colored("--------","red"),colored("REQUEST_RACER","magenta"),colored("---------","red"))
print(colored("------------by-m00n-------------\n","blue"))
data = ""
header = {}

def fun_start():
 try:
  method = sys.argv[1]
 except IndexError:
  print(colored("""[GET]  $ python thread000.py -get -u https://example.com -t [thread_count]
[post] $ python thread000.py -post -u https://example.com -t [thread_count] ""","magenta")) 
  pass
 else:
  try:
   urli = sys.argv[2]
  except IndexError:
   print(colored("""[GET]  $ python thread000.py -get -u https://example.com -t [thread_count]
[post] $ python thread000.py -post -u https://example.com -t [thread_count] ""","magenta"))
   pass
  else:
   if urli == '-u': 
    try:
     inp2 = sys.argv[3]
    except IndexError:
     print(colored("""[GET]  $ python thread000.py -get -u https://example.com -t [thread_count]
[post] $ python thread000.py -post -u https://example.com -t [thread_count] ""","magenta"))
     pass
    else:
     url = f"{inp2}"
     try:
      threadi = sys.argv[4]
     except IndexError:
      print(colored("""[GET]  $ python thread000.py -get -u https://example.com -t [thread_count]
[post] $ python thread000.py -post -u https://example.com -t [thread_count] ""","magenta"))
      pass
     else:
      if threadi == '-t':
       try:
        inp1 = int(sys.argv[5])
       except IndexError:
        print(colored("""[GET]  $ python thread000.py -get -u https://example.com -t [thread_count]
[post] $ python thread000.py -post -u https://example.com -t [thread_count] ""","magenta"))
        pass
       else: 
        def kk(i):
         
         if method == "-get":       
          status = requests.get(url,data=data,headers=header).status_code
         if method == "-post":
          status = requests.post(url).status_code
         print(colored(f" [>] {status}","blue"),colored(f' [Thread No] -> {i} ','red'))
        for i in range(1,inp1+1):
         t = Thread(target=kk,args=(i,))
         t.start()
         
   else:
    print("-u to specify the url")



fun_start()
 
