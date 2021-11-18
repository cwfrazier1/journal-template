#!/usr/bin/python

import os
import time
from os import path
from datetime import datetime

now = datetime.now()

date = now.strftime("%B %d %Y")
dateH = now.strftime("%B %d, %Y")
month = now.strftime("%B")

year = str(datetime.now().year)
month = str(datetime.now().month)

directory="/volume1/dropbox/Ulysses/Journal/"+year+"/"

if path.exists(directory) == False: 
    os.popen("mkdir "+directory)
    time.sleep(5)

directory=directory+month+"/"

if path.exists(directory) == False: 
    os.popen("mkdir "+directory)
    time.sleep(5)

os.popen("touch \""+directory+date+".md\"")

file = open(directory+date+".md","w")
file.write("# "+dateH+"\n\n##Three Positive Things:\n-")
file.close()
