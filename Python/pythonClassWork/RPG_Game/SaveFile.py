
import SignUp as SU
import Equipment as Ep
import GameList as GameList
import Person as Ps
import pickle



def SaveFile():
    #persons
    f=open('persons.txt','wb')
    pickle.dump(Ps.persons,f)
    f.close()

    f=open('users.txt','wb')
    pickle.dump(SU.users,f)
    f.close()

    f=open('equipments.txt','wb')
    pickle.dump(Ep.equipments,f)
    f.close()
    exit()

    pass