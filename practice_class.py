class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

# 드랍십
dropship = FlyableUnit() # 다중상속에서는 super() 쓸 경우, 우선 상속만 출력됨