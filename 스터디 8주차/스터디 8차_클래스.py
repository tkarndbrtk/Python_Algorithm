"""
# 마린 : 공격 유닛, 군인, 총 사용
name= 'marine' # Unit name
hp = 40 # Unit Hp
damage = 5 # power of Unit

print(f"{name} 유닛이 생성되었습니다.")
print(f"체력 {hp}, 공격력 {damage}\n")

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음. 일반모드 / 시즈모드
tank_name = "tank"
tank_hp = 150
tank_damage = 35

print(f"{tank_name} 유닛이 생성되었습니다.")
print(f"체력 {tank_hp}, 공격력 {tank_damage}\n")

def attack(name, location, damage):
    print(f"{name} : {location} 방향으로 적군을 공격합니다.[공격력 {damage}]")

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
"""
# 탱크가 여러 개 일 때, 어떻게 표현할까? -->class
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # __init__ 파이썬에서 사용되는 생성자
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛이 생성되었습니다.")
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다.[속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -=damage # 여
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <=0:
            print(f"{self.name} : 파괴되었습니다.")

# 공격 유닛
class AttackUnit(Unit): # 부모와 자식
    def __init__(self, name, hp, speed, damage): # __init__ 파이썬에서 사용되는 생성자
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다.\
            [공격력 {self.damage}]")

#마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp> 10:
            self.hp -=10
            print(f"{self.name}: 스팀팩을 사용합니다.(Hp 10 감소)")
        else:
            print(f"{self.name}: 체력이 부족하여 스팀팩을 사용할 수 없습니다.")

class Tank(AttackUnit):
    #시즈모드 : 탱크를 고정시켜, 더 높은 파워로 공격 가능, 이동불가
    seize_developed = False # 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.set_seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        # 현재 시즈모드가 아님
        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *=2
            self.seize_mode = True
        else:
            print(f"{self.name} : 시즈모드를 해제합니다.")
            self.damage /=2
            self.seize_mode = False
            
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.cloaked = False # 클로킹 모드 (x 상태)

    def cloaking(self):
        if self.cloaked == True:
            print(f"{self.name} : 클로킹 모드를 해제합니다.")
            self.cloaked = False
        else: # 클로킹 모드 설정
            print(f"{self.name} : 클로킹 모드로 전환합니다.")
            self.cloaked = True



# 공중유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. \
            [속도 {self.flying_speed}]")
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, flying_speed, damage):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[알림] 플레이어님이 게임을 퇴장하였습니다.")

marine1 = AttackUnit("marine", 40, 5, 5)
marine2 = AttackUnit("marine", 40, 5, 5)
tank = AttackUnit("tank", 150, 6, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹
wraith1 = AttackUnit("wraith", 80, 15, 5)
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것
wraith2 = AttackUnit("wraith", 80, 15, 5)
wraith2.cloaking = True
if wraith2.cloaking == True:
    print(f"{wraith2.name} 는 현재 클로킹 상태입니다.")

    
# 메딕 : 의무병
# 파이어 뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("firebat", 50, 5, 16)
firebat1.attack("5시")

# 공격 두번 받음
firebat1.damaged(25)
firebat1.damaged(25)

#드랍십 : 공중 유닛, 수송기
#발키리 : 공중 공격 유닛
valkyrie = FlyableAttackUnit("valkyrie", 200, 60, 5)
valkyrie.fly(valkyrie.name, "3시")

# 벌쳐 : 지상 유닛, 기동성이 좋다
vulture = AttackUnit("vulture", 80, 10, 20)

# 배틀크루저 : 공중유닛, 체력 좋음, 공격력 좋음
battlecruiser = FlyableAttackUnit("battlecruiser", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")

# 날아다니는놈은 fly 지상은 move 함수를 구분지어야함 --> 귀찮아
battlecruiser.move("9시")



# 게임 시작
game_start()

# 마린 3기 생성

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄 관리( 생성된 모든 유닛 append)

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전구 ㄴ이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.cloaking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit













