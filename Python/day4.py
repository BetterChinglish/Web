#coding:utf-8

#1
import random

def main(str):
    dic={}
    print str
    
    #制定列表li
    for i in 'abcdefghijklmnopqrstuvwxyz':
        dic[i]=0   
        
    #判断str字符串
    for i in str:
        dic[i]+=1
        
    #输出
    big=0
    sum=[]
    for i in dic:
        print i,"出现了：", dic[i], "次"
        if dic[i] > big:
            big=dic[i]
    print '\n'
    print "最大的是："
    for i in dic:
        if dic[i]==big:
            print i,' 出现了： ',dic[i],' 次'
          
def getStr():
    str=''
    for i in range(100):
        num=random.randint(97,122)
        str_temple=chr(num)
        str+=str_temple
    return str
          
main(getStr())     
      
     

#2 输出星期几
import time

def getDay():
    str=time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
    print(str.split()[0])

getDay()

coding:utf-8


#3 排序
def bull(a): 
    for m in range(len(a)-1):
        for n in range(len(a)-1-m):
            if(a[n]>a[n+1]):
                temple=a[n] 
                a[n]=a[n+1]
                a[n+1]=temple
    return a  

def fast(a):
    if(len(a)>=2):
        mid=a[len(a)//2]

        left=[]
        rigth=[]

        a.remove(mid)

        for i in a:
            if i<mid:
                left.append(i)
            else:
                right.append(i)

        return fastSort(left)+[mid]+fastSort(right)
    else:
        return a

def insert(a):
    for i in range(1,len(a)):
        temple=a[i]
        j=i-1 
        while(j>=0 and temple<a[j]):
            a[j+1]=a[j] 
            a[j]=temple
            j-=1
    return a


def select(a):
    for i in range(len(a)-1):
        m = i 
        for j in range(i+1,len(a)):
            if(a[j]<a[m]):
                m = j 
        temple=a[i]
        a[i]=a[m]
        a[m]=temple   
    return a
