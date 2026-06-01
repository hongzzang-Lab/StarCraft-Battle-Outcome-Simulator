class Unit:
    def __init__(self, name, hp,speed):
        self.name = name #멤버변수 : class내에서 정의된 변수 name,hp,damage
        self.hp=hp
        self.speed = speed 


    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"\
              .format(self.name, location, self.speed))



#건물 
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
       # Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0) #super()할땐 self값 뺴기, #부모 class로부터 상속 받을 때의 표현 
        self.location=location

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable): #상속 되어있다고 init함수를 통해 한번 더 정의하기 
    def __init__(self):
        super().__init__()
        