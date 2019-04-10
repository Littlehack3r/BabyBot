#Babybot.py
#Shannon McHale
#HackerThon00 Project
#Feb 9, 2019
#Baby bot is a simple bot that goes to a local host site.
#Takes commands from the site and runs them. 

#request out to server
#get commands
#exec commands
#sleep
#wake up do it again
#sleep 

import json
import requests
import subprocess
import time

while True:
    bot = 'bot1'

    #reaches out to the webserver
    web = requests.get('http://localhost:8080/getcommands/'+ bot)
    print(web.text)

    
    lst = json.loads(web.text)  #lst of commands 

    print(subprocess.check_output(lst[0]))  #runs the commands in a terminal 

    bot = 'bot2'
    web = requests.get('http://localhost:8080/getcommands/'+ bot)
    print(web.text)


    lst = json.loads(web.text)  #lst of commands 

    #get each command
    for i in lst:
        k = i.split(" ")
        print(subprocess.check_output(k))

    #rest bot
    time.sleep(10)