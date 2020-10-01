


#2 输出星期几
import time

def getDay():
    str=time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
    print(str.split()[0])

getDay()