import random  #random 모듈을 불러온다

# 일반 유닛
from Attack import AttackUnit
from Attack import Unit

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)

     #스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    
    def stimpack(self):
        if self.hp>10:
            self.hp -=10
            print("{0} : 스팀팩을 사용합니다. (HP 10감소)".format(self.name))

        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
     
# 탱크
class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능,이동불가
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크",150,1,35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈모드가 아닐 때 --> 시즈모드 
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *=2
            self.seize_mode = True

        # 현재 시즈모드일 때 --> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /=2
            self.seize_mode =False

from flyableunit import Flyable
             
#공중 유닛 클래스  #2개를 상속받아서 정의함      
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage)#지상 speed 0 
        Flyable.__init__(self,flying_speed)

    def move(self,location):  #Flyableattackunit class안에서의 move함수를 정의하여 공중유닛은 이 class내의  move함수를 사용케 함 
        print("[공중 유닛 이동]")
        self.fly(self.name , location)
           
#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked=True #클로킹 모드 (해제상태)

    def clocking(self):
        if self.clocked == True: #클로킹 모드 --> 모드 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False

        else:  #클로킹 모드 해제 --> 모드 설정
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked=True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("player : gg") #game over
    print("[player] 님이 게임에서 퇴장하셨습니다.")


#실제 게임 진행

game_start()

#마린 3기 생성
m1 = Marine()
m2= Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

#레이스 1기 생성
w1= Wraith()

#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동 
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비(마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit,Marine):  # unit이 marine class의 것인지 판단 
        unit.stimpack()
    
    elif isinstance(unit,Tank):
        unit.set_seize_mode()

    elif isinstance(unit,Wraith):
        unit.clocking()


# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(random.randint(5,21))

#게임 종료
game_over()








