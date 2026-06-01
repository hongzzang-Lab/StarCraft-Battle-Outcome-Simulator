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
        pass

#서플라이 디폿 : 건물 , 1개 건물 = 8 유닛
supply_depot = BuildingUnit("서플라이 디폿",500,"7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass
