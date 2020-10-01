import Person as Ps 
import SignUp as SU
import SignIn as SI
import Equipment as Ep
import GameList as GL
import SaveFile as SF

def printMenu():
    print('''
        1 登录
        2 注册
        3 关于我
        0 退出游戏
    ''')

def admin_menu():
    while True:
        print('''
        1 添加装备
        2 查看装备信息
        3 删除装备信息
        4 添加游戏关卡
        5 查看游戏关卡
        6 删除游戏关卡
        7 查看玩家信息
        ''')
        admin_choice=input('请输入您的选择：')
        if admin_choice=='back':
            return
        if admin_choice=='1':
            Ep.newEquipment()
            pass
        if admin_choice=='2':
            Ep.printEquipment()
        if admin_choice=='3':
            while True:
                n=input('请输入您要删除的装备的序号或输入 back 返回')
                if n == 'back':
                    break
                n=int(n)
                Ep.deletEquipment(n)
        if admin_choice=='4':
            GL.newGame()
            pass
        if admin_choice=='5':
            GL.printGames()
            pass
        if admin_choice=='6':
            while True:
                n=input('请输入您要删除的游戏关卡的序号或输入 back 返回')
                if n == 'back':
                    break
                n=int(n)
                GL.deleteGame(n)
        if admin_choice=='7':
            n=0
            for person in Ps.persons:
                print('序号：',n)
                person.printPerson()
                print('\n')
                n=n+1
            del n
    pass

def firstGamingGuide(user_name,user_password):
    if SI.users[user_name][1]==0:
        name=input('请输入您的名字：')
        sex=input('请输入您的性别(男\\女):')
        age=input('请输入您的年龄：')
        person=Ps.Person(name,sex,age)
        Ps.persons.append(person)
        SI.users[user_name]=[user_password,1,len(Ps.persons)-1]#Ps.persons[Ps.persons_number]
        print('创建成功')
    else:
        return

def gameMenu(user_name,user_password):
    firstGamingGuide(user_name,user_password)
    print('您的基本信息：')
    Ps.persons[SI.users[user_name][2]].printPerson()
    while True:
        print('''
        1 查看关卡
        2 选择关卡
        3 查看背包
        4 穿戴物品
        5 查看人物属性及装备
        0 保存并退出
        ''')
        choice=input('请输入您的选择：')
        if choice=='1':
            GL.printGames()
        if choice=='2':
            pass
        if choice=='3':
            n=0
            for num in Ps.persons[SI.users[user_name][2]].person_bag:
                print('背包序号：',n)
                Ep.equipments[num].printEquipment()
                n=n+1
        if choice=='4':
            num=input('请输入您要装备的物品的背包序号或back返回：')
            if num=='back':
                continue
            elif num not in Ps.persons[SI.users[user_name][2]].person_bag:
                print('没有此装备！')
                continue
            else:
                Ps.persons[SI.users[user_name][2]].updatEquipment(num)
        if choice=='5':
            Ps.persons[SI.users[user_name][2]].printPerson()
        if choice=='0':
            SF.SaveFile()
            