# coding:utf-8

import os
import re

filename="student.txt"
stuInfo=[]

def main():
    recoverFile()
    while True:
        printMenu()
        key=int(input('please enter your choice:'))
        if key==1:
            print("you can enter 'back' to back")
            addInfo()
        elif key==2:
            print("you can enter 'back' to back")
            delInfo()
        elif key==3:
            print("you can enter 'back' to back")
            modifystuInfo()
        elif key==4:
            showstuInfo()
        elif key==5:
            saveFile()
        elif key==0:
            quitConfirm=input('quit? remember to save your file first! please enter yes or no)')
            if quitConfirm=="yes":
                print("thanks for using!")
                break
            else:
                print("wrong!enter again please")
            
        
#show menu              
def printMenu():
    print ('''
       1 add
       2 delete
       3 modify
       4 show
       5 save
       0 quit
       
       ''')

#add student
def addInfo():
    while True:
        
        stuName=input("name:")
        if stuName=='back':
            return
        stuSex=input("sex:")
        stuId=input("id:")
        info={}
        info['name']=stuName
        info['sex']=stuSex
        info['id']=stuId
        stuInfo.append(info)
        print("sucessful")

    
#delete student
def delInfo():
    while True:
        showstuInfo()
        delNumber=input('number you wanna delete:')
        if delNumber=='back':
            return 
        else:
            delNumber=int(delNumber)
        del stuInfo[delNumber]
        print("sucessful")


#change one's information
def modifystuInfo():
    while True:
        showstuInfo()
        id=input('id you wanna change:')
        if id=='back':
            return
        else:
            id=int(id)
        stuName=input('new name:')
        stuSex=input('new sex:')
        stuId=input('new id:')
        charge=input("sure to change? enter yes or no")
        if charge=="yes":
            stuInfo[id]['name']=stuName
            stuInfo[id]['sex']=stuSex
            stuInfo[id]['id']=stuId
        elif charge=="no":
            print("quit")
            charge2=input("modify another? enter yes or no")
            if charge2=="yes":
                modifystuInfo()
            elif charge2=="no":
                return 

#show all students' message
def  showstuInfo():
    print("all students' message:")
    print("num      name        sex     id    ")
    i=0
    for info in stuInfo:
        print("%d       %s      %s      %s" %(i,info['name'],info['sex'],info['id']))
        i+=1

#save up the information
def saveFile():
    fo=open(filename,"w")
    for info in stuInfo:
        str=info['name']+' '+info['sex']+' '+info['id']
        fo.write(str)
        fo.write('\n')

    fo.close()

#recover the information
def recoverFile():
    fo=open(filename,'r')
    contents=fo.readlines()
    for msg in contents:
        msg=msg.strip('\n')
        student={'name':' ','sex':' ','id':""}
        student['name'],student['sex'],student['id']=msg.split(' ')
        stuInfo.append(student)
    fo.close()


main()