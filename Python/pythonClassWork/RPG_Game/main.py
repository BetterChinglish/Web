import Person as Ps
import Equipment as Ep
import Menu as Mn
import AboutMe as AM
import SignUp as SU
import Recover as Rc
import SaveFile as SF
import SignIn as SI



def GameMain():
    
    Rc.Recover()
    while True:
    
        Mn.printMenu()

        choice=input('输入您的选择: ')
        if choice == '3':
            AM.AboutMe()
        if choice == '2':
            SU.SignUp()
        if choice == '1':
            SI.SignIn()
        if choice == '0':
            SF.SaveFile()


GameMain()