
from SignUp import users
import Menu as Mn

def SignIn():
        name=input('请输入你的用户名：')
        if name == 'qsj':
            if input('请输入管理员密码：')=='123321':
                Mn.admin_menu()
            
        elif name not in users:
            print('用户名不存在！')
        else:
            getPassword(name)

def getPassword(name):

    password=input('请输入你的密码或输入back返回：')
    if password=='back':
        print('登录失败！')
        return
    elif password==users[name][0]:
        print('登录成功！')
        Mn.gameMenu(name,password)    
    else:
        print('密码错误！')
        getPassword(name)
    