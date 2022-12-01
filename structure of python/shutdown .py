from logging import shutdown
import os 

shutdown=input("do you want to shutdown(y/n):")

if shutdown=="no":
    exit()
else:
    os.system("shutdown/s /t 1")
