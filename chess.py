from abc import abstractmethod,ABCMeta
class chess(metaclass=ABCMeta):
    def __init__(self,piece_name):
        self.piece_name=piece_name

    @abstractmethod
    def movement(self):
        pass


class piece(chess):
    def __int__(self,piece_name,movement):
        super().__init__(piece_name)
    def movement(self,movement):
        self._movement=movement
        return self._movement



hourse=piece("hourse")
#hourse.movement("L shape")
print(hourse.piece_name)
print(hourse.movement("L shape"))