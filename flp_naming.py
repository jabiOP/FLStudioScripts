import datetime, os, shutil, subprocess, platform

## This script creates a .flp according to my naming system
## by jabi @onepathJB 

#Funtion to check/create folder
def check (n):
    if not os.path.exists(n):
        os.mkdir(n)
        return True

#Function to open FL Studio with file
def fruity (filepath):
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)

#FLPs Directory and Template
flps = YOUR_OWN_PATH_HERE
template = YOUR_OWN_PATH_HERE

#Getting date to use as filename
date = datetime.datetime.now()

#Month folder
month = date.strftime("%m") + "_" + date.strftime("%Y")
mf = flps + month

#Day Folder
day = date.strftime("%m") + date.strftime("%d") + date.strftime("%y") 
df = mf + "/" + day

#Monthly folder check/create
check (mf)

#Day folder check/create
for x in range(97, 123):
    if check (df + chr(x)):
        file = df + chr(x) + "/" + day + chr(x) + ".flp"
        shutil.copyfile(template, file) 
        fruity (file)
        break
