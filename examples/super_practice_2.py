
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable): #상속 되어있다고 init함수를 통해 한번 더 정의하기 
    def __init__(self):
       # super().__init__() #문제점 : FlyableUnit을 호출하면 상속된 2개의 class가 둘다 반응하는 것이 아니라 
        #class Flyableunit(unit,flyable)중 unit class만 통과해서 실행시킨다 
        Unit.__init__(self)
        Flyable.__init__(self) #다중상속의 경우에는 이렇게 초기화 시켜준다.
#드랍쉽
dropship = FlyableUnit()