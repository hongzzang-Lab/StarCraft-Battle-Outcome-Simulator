class Unit:
    def __init__(self, name, hp):
        self.name = name #멤버변수 : class내에서 정의된 변수 name,hp,damage
        self.hp=hp


#공격 유닛 #Unit class에 의해 상속받음
class AttackUnit(Unit):
     def __init__(self, name, hp, damage):
        Unit.__init__(self,name,hp) #unit class에서 가져왔기에 저렇게 표기
        self.damage=damage #Unit class에는 없는 내용을 추가 

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

#드랍쉽 : 공중 유닛, 수송기, 마린/파이어뱃/탱크 등을 수송 . 공격x 

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed


    def fly(self,name, location):
        print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]"\
              .format(name,location,self.flying_speed))
#공중 유닛 클래스  #2개를 상속받아서 정의함      
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)

#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie=FlyableAttackUnit("발키리",200,6,5) #class FlyableAttackunit의 __init 함수안의 매개변수 4개
valkyrie.fly(valkyrie.name, "3시") #바로 윗줄에서 valkyrie.name값에 "발키리"가 들어감 그리고 fly함수는 clalss flyable것 이므로 매개변수인 name과 location값을 받는 것
