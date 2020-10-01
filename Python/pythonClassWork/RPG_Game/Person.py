
import Equipment as Ep
import os
import pickle


persons=[]

class Person:
    #人物基本属性
    name=' '#人物姓名
    sex=' '#人物性别
    age=' '#人物年龄
    levels=1#人物等级
    hp=100 #人物总血量
    hp_temple=100 #人物当前血量
    experiences=0#当前经验
    level_experiences=100#升级所需经验


    #人物部位装备
    head='工地塑料头盔'#头部装备
    body='破烂衬衫'#身体装备
    legs='破洞牛仔裤'#腿部装备
    shoes='拖鞋'#鞋子
    gloves='一次性手套'#手套
    rings='狗尾巴草戒指'#戒指
    equipment_now=[0,1,2,3,4,5]

    #人物能力属性
    physical_attack=10#物理攻击
    physical_defense=5#物理防御
    magic_attack=10#法术攻击
    magic_defense=5#法术防御
    speed=10#速度

    #人物背包
    person_bag=[]

    #初始化人物姓名，性别，年龄
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

    #更新装备
    #传入背包第num个装备(是总装备序号)
    def updateEquipment(self,num):
        if Ep.equipments[self.person_bag[num]].place=='head':
            self.person_bag.append(self.equipment_now[0])#当前头部装备卸下，放入背包
            self.head=Ep.equipments[self.person_bag[num]].place#当前头部装备名称更新
            self.physical_attack+=Ep.equipments[self.person_bag[num]].physical_attack
            self.physical_defense+=Ep.equipments[self.person_bag[num]].physical_defense
            self.magic_attack+=Ep.equipments[self.person_bag[num]].magic_attack
            self.magic_defense+=Ep.equipments[self.person_bag[num]].magic_defense
            self.speed+=Ep.equipments[self.person_bag[num]].speeds
            self.equipment_now[0]=self.person_bag[num]#当前装备列表更新
        elif Ep.equipments[self.person_bag[num]].place=='body':
            self.person_bag.append(self.equipment_now[1])
            self.head=Ep.equipments[self.person_bag[num]].place
            self.physical_attack=Ep.equipments[self.person_bag[num]].physical_attack
            self.physical_defense=Ep.equipments[self.person_bag[num]].physical_defense
            self.magic_attack=Ep.equipments[self.person_bag[num]].magic_attack
            self.magic_defense=Ep.equipments[self.person_bag[num]].magic_defense
            self.speed=Ep.equipments[self.person_bag[num]].speeds
        elif Ep.equipments[self.person_bag[num]].place=='legs':
            self.person_bag.append(self.equipment_now[2])
            self.head=Ep.equipments[self.person_bag[num]].place
            self.physical_attack=Ep.equipments[self.person_bag[num]].physical_attack
            self.physical_defense=Ep.equipments[self.person_bag[num]].physical_defense
            self.magic_attack=Ep.equipments[self.person_bag[num]].magic_attack
            self.magic_defense=Ep.equipments[self.person_bag[num]].magic_defense
            self.speed=Ep.equipments[self.person_bag[num]].speeds
        elif Ep.equipments[self.person_bag[num]].place=='shoes':
            self.person_bag.append(self.equipment_now[3])
            self.head=Ep.equipments[self.person_bag[num]].place
            self.physical_attack=Ep.equipments[self.person_bag[num]].physical_attack
            self.physical_defense=Ep.equipments[self.person_bag[num]].physical_defense
            self.magic_attack=Ep.equipments[self.person_bag[num]].magic_attack
            self.magic_defense=Ep.equipments[self.person_bag[num]].magic_defense
            self.speed=Ep.equipments[self.person_bag[num]].speeds
        elif Ep.equipments[self.person_bag[num]].place=='gloves':
            self.person_bag.append(self.equipment_now[4])
            self.head=Ep.equipments[self.person_bag[num]].place
            self.physical_attack=Ep.equipments[self.person_bag[num]].physical_attack
            self.physical_defense=Ep.equipments[self.person_bag[num]].physical_defense
            self.magic_attack=Ep.equipments[self.person_bag[num]].magic_attack
            self.magic_defense=Ep.equipments[self.person_bag[num]].magic_defense
            self.speed=Ep.equipments[self.person_bag[num]].speeds
        elif Ep.equipments[self.person_bag[num]].place=='rings':
            self.person_bag.append(self.equipment_now[5])
            self.head=Ep.equipments[self.person_bag[num]].place
            self.physical_attack=Ep.equipments[self.person_bag[num]].physical_attack
            self.physical_defense=Ep.equipments[self.person_bag[num]].physical_defense
            self.magic_attack=Ep.equipments[self.person_bag[num]].magic_attack
            self.magic_defense=Ep.equipments[self.person_bag[num]].magic_defense
            self.speed=Ep.equipments[self.person_bag[num]].speeds
        del self.person_bag[num]
        print('装备更换成功！')


    def getLevel(self,experiences):
        self.experiences+=experiences

    def updateLevel(self):
        if self.experiences>(self.levels)*100:
            self.experiences-=(self.experiences)*100
            self.levels+=1
            self.level_experiences=self.levels*100-self.experiences

    def printPerson(self):
        print('姓名：',self.name,\
            '\n性别：',self.sex,\
            '\n年龄：',self.age,\
            '\n等级：',self.levels,\
            '\n升级所需经验：',self.level_experiences,\
            '\n装备如下：'\
                #pass
            )
       

def deletePerson(n):
    del persons[n]
    print('删除成功！')
    return           
        

# if os.path.getsize('persons.txt')==0:
#     persons=[]
# else:
#     f=open('persons.txt','rb')
#     persons.append(pickle.load(f))
#     f.close()