class Unit:
    def __init__(self, name, hp, damage):
        self.name = name #멤버변수 : class내에서 정의된 변수 name,hp,damage
        self.hp=hp
        self.damage=damage
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))



marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)  #마리니과 탱크는 유닛 class의 인스턴스임 and 객체라고 함
tank = Unit("탱크", 150, 35)

#레이스 : 공중 유닛, 비행기 , 클로킹(스텔스 기능)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

#마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(뺏기)
wraith2= Unit("레이스",80,5)
wraith2.clocking = True #wraith2 에 추가로 clocking 이라는 멤버변수를 할당하고 그 값에 True를 넣은 것 (위의 class에는 없는 것을 추가!)


if wraith2.clocking==True:
    print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name))

          