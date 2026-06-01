class Unit:
    def __init__(self, name, hp,speed):
        self.name = name #멤버변수 : class내에서 정의된 변수 name,hp,damage
        self.hp=hp
        self.speed = speed 


    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도 {2}]"\
              .format(self.name, location, self.speed))


#공격 유닛
class AttackUnit(Unit):
     def __init__(self, name, hp, speed ,damage):
        Unit.__init__(self, name, hp,speed)
        self.damage=damage
        
     def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격.[공격력 {2}]."\
              .format(self.name,location,self.damage)) 
        #self.name, self.damage는 위에서 정의된 것을 쓴다는 것 
        #self가 없는 location 같은 경우에는 함수 attack에서 전달받은 location값을 쓴다는 것
    
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
        AttackUnit.__init__(self,name,hp,0,damage)#지상 speed 0 
        Flyable.__init__(self,flying_speed)

    def move(self,location):  #Flyableattackunit class안에서의 move함수를 정의하여 공중유닛은 이 class내의  move함수를 사용케 함 
        print("[공중 유닛 이동]")
        self.fly(self.name , location)


#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie=FlyableAttackUnit("발키리",200,6,5) #class FlyableAttackunit의 __init 함수안의 매개변수 4개
valkyrie.fly(valkyrie.name, "3시") #바로 윗줄에서 valkyrie.name값에 "발키리"가 들어감 그리고 fly함수는 clalss flyable것 이므로 매개변수인 name과 location값을 받는 것

#벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐",80,10,20)

#배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

vulture.move("11시")
battlecruiser.move("9시") #여기의 move함수는 Class flyableattackunit에 연결되어있는 move함수다 
#vulture는 공중관련 class를 상속x battlecruiser는 공중관련 class 상속 ㅇ
