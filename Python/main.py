#coding:utf-8

import os
import re
import string

users={}
books=[]




def printMenu():
    print(' 1 sign in\n 2 sign up\n 0 save and exit\n')

def printMenu_normal():
    print(' 1 show books\n 2 borrwo books\n')


def printMenu_admin():
    print(' 1 borrow books\n 2 new books\n 3 show books\n 0 exit\n')




def print_books():
    sum=0
    print('书籍如下：')
    for book in books:
        sum+=1
        print('序号：',sum,'\n书名：', book['name'], '\n数量：',book['amount'])
        print('\n')



def recover():
    #恢复书
    file_books=open('books.txt','r')
    contents=file_books.readlines()
    for msg in contents:
        msg=msg.strip('\n')
        book={'name':' ','amount':' '}
        book['name'],book['amount']=msg.split(' ')
        book['amount']=int(book['amount'])
        books.append(book)
    file_books.close()

    #恢复用户
    file_users=open('users.txt','r')
    contents=file_users.readlines()
    for msg in contents:
        msg=msg.strip('\n')
        name,password=msg.split(' ')
        users[name]=password
    file_users.close()
    

def save():
    #保存书
    file_book=open('books.txt','w')
    for book in books:
        str1=book['name'] + ' ' + str(book['amount'])
        file_book.write(str1)
        file_book.write('\n')
    file_book.close()

    #保存用户
    file_user=open('users.txt','w')
    for key in users.keys():
        str1=key+' '+users[key]
        file_user.write(str1)
        file_user.write('\n')
    file_user.close()

#查询是否存在用户
def find_member(name):
    if name in users:
        return True
    else:
        return False

#查询账户对应密码是否正确
def true_password(name,password):
    global users

#mian
def main():


    global books
    global users

    recover()

    while True:

        printMenu()

        choice=input("enter your choice:")
        if choice not in ['1','2','0']:
            print("wrong! please enter a number (0~2)")
            continue

        choice=int(choice)

        #退出程序
        if choice==0:
            save()
            return 
        
        #登录
        if choice==1:
            while True:
                
                name=input('(sign in)enter your name or \' back \' to back :')
                if name=='back':
                    break
                
                #管理员登录
                if name=='admin':
                    password=input("enter your password:")
                    if password=='admin':
                        print("登录成功")
                        while True:
                            printMenu_admin()
                            choice_admin=input('enter your choice or \'back\' to back:')
                            if choice_admin=='back':
                                break
                            if choice_admin=='0':
                                save()
                                return 
                            if choice_admin=='1':
                                while True:
                                    print_books()
                                    whether_borrow_book=input('借书请输入序号，或输入back返回（除‘back’以外请勿输入非数字）')
                                    if whether_borrow_book=='back':
                                        break
                                    whether_borrow_book=int(whether_borrow_book)
                                    if books[whether_borrow_book-1]['amount']>0:
                                        books[whether_borrow_book-1]['amount']-=1
                                        print('已记录，您现在可以将书带走')
                                    else:
                                        print("剩余0本，请重新选择！")
                            if choice_admin=='2':
                                while True:
                                    book_name=input('添加书籍请输入书名(或back返回上一级)：')
                                    if book_name=='back':
                                        break
                                    book_amount=int(input('请输入此书数量：'))
                                    new_book={'name':book_name,'amount':book_amount}
                                    books.append(new_book)
                                    print('添加成功！')
                            if choice_admin=='3':
                                print_books()

                                

                        
                #普通用户登录
                elif name in users:
                    password=input('enter your password:')
                    if users[name]==password:
                        print("登录成功！")
                        while True:
                            printMenu_normal()
                            choice_normal=input('enter your choice or \'back\' to back:')
                            if choice_normal=='back':
                                break
                            if choice_normal=='0':
                                save()
                                return 
                            if choice_normal=='1':
                                print_books()
                            if choice_normal=='2':
                                while True:
                                    print_books()
                                    whether_borrow_book=input('借书请输入序号，或输入back返回（除‘back’以外请勿输入非数字）')
                                    if whether_borrow_book=='back':
                                        break
                                    whether_borrow_book=int(whether_borrow_book)
                                    if books[whether_borrow_book]['amount']>0:
                                        books[whether_borrow_book]['amount']-=1
                                        print('已记录，您现在可以将书带走')


                    else:
                        print("用户名或密码错误！")
                        continue
                else:
                    print('用户不存在,请重新输入!')
                    continue
        

        #注册
        if choice==2:

            while True:
                name=input('your name or \' back\' to back :')
                if name=='back':
                    break
                if name not in users:
                    password=input('your password:') 
                    users[name]=password
                    print("注册成功！")
                    break


    save()
main()