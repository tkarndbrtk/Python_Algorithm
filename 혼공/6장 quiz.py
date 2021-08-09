from math import*
from random import*
minute = randint(5,50)
person = 0
for customer in range(1,51): # 1 ~ 50 이라는 수 (승객)
    if 5<=minute<=15:
        print("[O]{0}번째 손님(소요시간 : {1}분)".format(customer, minute))
        minute = randint(1,50)
        person +=1
    else:
        print("[ ]{0}번째 손님(소요시간 : {1}분)".format(customer, minute))
        minute = randint(1,50)
print("총 탑승 승객 : {0} 분".format(person))