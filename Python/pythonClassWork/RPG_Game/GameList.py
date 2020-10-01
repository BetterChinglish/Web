import Equipment as Ep
import random

games=[]

class Game:
    #关卡数据
    game_name=' '
    boss_name=''
    boss_level=0
    boss_Pattack=0
    boss_Pdefense=0
    boss_Mattack=0
    boss_Mdefense=0
    boss_speed=0

    #关卡掉落装备数据
    getEquipmentNum=[]
    
    experiences=0
    
    def __init__(self,game_name,boss_name,boss_level,boss_Pattack,boss_Pdefense,boss_Mattack,boss_Mdefense,boss_speed,getEquipmentNum):
        self.game_name=game_name
        self.boss_name=boss_name
        self.boss_level=boss_level
        self.boss_Pattack=boss_Pattack
        self.boss_Pdefense=boss_Pdefense
        self.boss_Mattack=boss_Mattack
        self.boss_Mdefense=boss_Mdefense
        self.boss_speed=boss_speed
        self.getEquipmentNum=getEquipmentNum
    
    
    #玩家获得经验值：
    def getExperiences(self):
        self.experiences=random.randint(self.boss_level*3,self.boss_level*7)

    #装备掉落
    def getEquitment(self): 
        list_temple=[]
        for i in range(len(self.getEquipmentNum)):
            n=random.randint(1,100)
            if Ep.equipments[self.getEquipmentNum[i]].rare_level >= n:
                list_temple.append(self.getEquipmentNum[i])
        return list_temple

def newGame():
    game_name=input('请输入关卡名称：')
    boss_name=input('请输入boss名称：')
    boss_level=int(input('请输入boss等级'))
    boss_Pattack=int(input('请输入boss攻击力：'))
    boss_Pdefense=int(input('请输入boss防御力：'))
    boss_Mattack=int(input('请输入boss法强：'))
    boss_Mdefense=int(input('请输入boss魔抗：'))
    boss_speed=int(input('请输入boss速度：'))
    Ep.printEquipment()
    str=input('请输入本关卡可能掉落的装备序号，使用空格隔开，回车确认：')
    getEquipmentNum=list(str.split())
    n=0
    for n in range(len(getEquipmentNum)):
        getEquipmentNum[n]=int(getEquipmentNum[n])
    game=Game(game_name,boss_name,boss_level,boss_Pattack,boss_Pdefense,boss_Mattack,boss_Mdefense,boss_speed,getEquipmentNum)
    games.append(game)
    print('添加成功')

def printGames():
    n=0
    for game in games:
        print('序号：',n,'\n\
        关卡名：',game.game_name,'\n\
        boss名：',game.boss_name,'\n\
        物理攻击与防御：',game.boss_Pattack,'    ',game.boss_Pdefense,'\n\
        法术攻击与防御：',game.boss_Mattack,'    ',game.boss_Mdefense,'\n')
        n=n+1

def deleteGame(n):
    del games[n]
    print('删除成功！')