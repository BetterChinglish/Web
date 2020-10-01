
import Person as Ps
import os
import pickle 

users={}

def SignUp():
    while True:
        name=input('请输入你的用户名或输入back返回：')
        if name=='back':
            return
        if name not in users:
            password_one=input('请输入你的密码：')
            password_two=input('请确认你的密码：')
            if password_one==password_two:
                users[name]=[password_one,0]
                print('注册成功！')
                return
            else:
                print('两次密码输入不相同！')
        else:
            print('用户名已存在')



# if os.path.getsize('users.txt')==0:
#     users={}
# else:
#     f=open('users.txt','rb')
#     users=(pickle.load(f))
#     f.close()