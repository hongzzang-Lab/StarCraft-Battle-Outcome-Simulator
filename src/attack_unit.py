
# 일반 유닛
class Unit:
    def __init__(self, name, hp,speed):
        self.name = name #멤버변수 : class내에서 정의된 변수 name,hp,damage
        self.hp=hp
        self.speed = speed 
        print("{0} 유닛이 생성되었습니다.".format(name))

class AttackUnit(Unit):
     def __init__(self, name, hp, speed, damage):
        Unit.__init__(self,name,hp,speed)
        self.damage=damage

     def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"\
              .format(self.name, location, self.speed))

     def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격.[공격력 {2}]."\
              .format(self.name,location,self.damage)) 
        #self.name, self.damage는 위에서 정의된 것을 쓴다는 것 
        #self가 없는 location 같은 경우에는 함수 attack에서 전달받은 location값을 쓴다는 것
     def damaged(self, damage):
         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
         self.hp-=damage
         print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
         if self.hp<=0:
             print("{0} : 파괴되었습니다.".format(self.name))
