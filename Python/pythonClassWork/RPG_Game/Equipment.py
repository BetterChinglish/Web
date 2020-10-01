import os
import pickle

equipments=[]
# if os.path.getsize('equipments.txt')==0:
#     equipments=[]
# else:
#     f=open('equipments.txt','rb')
#     equipments.append((pickle.load(f)))
#     f.close()

class Equipment:
    name=' '#装备名称
    place=' '#穿戴部位
    physical_attack=0#物理攻击
    physical_defense=0#物理防御
    magic_attack=0#法术攻击
    magic_defense=0#法术防御
    speed=0#速度
    rare_level=0 #装备稀有程度
    

    def __init__(self,name,place,Pattack,Pdefense,Mattack,Mdefense,speed,rare_level):
        self.place=place
        self.name=name
        self.physical_attack=Pattack
        self.physical_defense=Pdefense
        self.magic_attack=Mattack
        self.magic_defense=Mdefense
        self.speed=speed
        self.rare_level=rare_level
    
    def printEquipment(self):
        print(self.name,'\n','位置：',self.place,'\n物理攻击与防御加成：',self.physical_attack,self.physical_defense,'\n法术攻击与防御加成：',self.magic_attack,self.magic_defense,'\n速度加成：',self.speed,'\n稀有程度：',self.rare_level)

def newEquipment():
    print("如若输入错误，您将展示错误的信息给玩家，请务必注意")
    name=input('装备名称：')
    print('您的装备名称为：',name)
    place=input('您要创建哪个部位的装备？\n\
        请输入head,body,legs,shoes,gloves,rings\n')
    Pattack =int(input("请输入装备带来的物理攻击加成："))
    Pdefense=int(input("请输入装备带来的物理防御加成："))
    Mattack =int(input("请输入装备带来的法术攻击加成："))
    Mdefense=int(input("请输入装备带来的法术防御加成："))
    speed=int(input("请输入装备带来的移动速度加成："))
    rare_level=int(input('请输入装备的稀有程度：'))
    
    print('确认：')
    print(name,'\n','位置：',place,'\n物理攻击与防御加成：',Pattack,Pdefense,'\n法术攻击与防御加成：',Mattack,Mdefense,'\n速度加成：',speed,'\n稀有程度：',rare_level)
    choice=input('输入 确认 或 取消 以确认\\取消：')
    if choice=='确认':
        equipment=Equipment(name,place,Pattack,Pdefense,Mattack,Mdefense,speed,rare_level)
        equipments.append(equipment)
        print('添加成功！')
        del name,place,Pattack,Pdefense,Mattack,Mdefense,speed,rare_level
    else:
        print('已取消')

def printEquipment():
    n=0
    for equipment in equipments:
        print('装备列表序号：',n,'\n\
        装备名称：',equipment.name,'\n\
        装备部位：',equipment.place,'\n\
        装备物理攻击与防御加成：',equipment.physical_attack,'    ',equipment.physical_defense,'\n\
        装备法术攻击与防御加成：',equipment.magic_attack,'    ',equipment.magic_defense,'\n\
        装备速度加成：',equipment.speed,'\n')
        n=n+1

def deletEquipment(n):
    del equipments[n]
    print('删除成功！')