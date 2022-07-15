from abc import abstractmethod,ABCMeta
class game(metaclass=ABCMeta):
    def __init__(self,name,color,shape):
        self.name=name
        self.color=color
        self.shape=shape

    @abstractmethod
    def movement(self):
        pass

    def speed(self):
        return "normal speed"


class character(game):
    def __int__(self,name,color,shape,movement,speed):
        super().__init__(name,color,shape)

    def movement(self,movement):
        self.movement=movement
        return self.movement
    def speed(self,speed):
        self.speed=speed
        return self.speed

mario=character("Mario",'Blue','Short')
print(mario.shape)
print(mario.movement('forward & jump'))
print(mario.speed('fast'))




