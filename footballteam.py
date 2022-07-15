from abc import abstractmethod,ABCMeta
class Team(metaclass=ABCMeta):
    def __init__(self,name,role,speed,DOB,salary,injury):
        self.name=name
        self.role=role
        self.speed=speed
        self.DOB = DOB
        self.salary= salary
        self.injury = injury

    def player_info(self):
        print("General Info\nname "+self.name+" role is "+self.role+ " speed is "+str(self.speed))

    @abstractmethod
    def has_injury(self):
        pass

class Player(Team):

    def __init__(self,name,role,speed,DOB,salary,injury):
        super().__init__(name,role,speed,DOB,salary,injury)

    def player_info(self):
        print("Detailed Info\nname " + self.name + "\nrole is " + self.role + "\nspeed is " + str(self.speed) + "\nDOB is "+self.DOB + "\nsalary is "+ self.salary)

    def has_injury(self):
        return self.injury


playerone = Player("MO Salah","RW",99,"1992-05-02","350K$",False)

playerone.player_info()
print(playerone.has_injury())