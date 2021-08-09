''' 
#2-1 연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10

print(2**3) #2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 나머지 1
print(5//3) # 몫구하기 1
print(10//3) # 3
print(10 > 3) # 비교연산 True
print(4 >= 7) # False
print(3==3) # True 같은지 비교할 땐 반드시 = 2개를 써줄 것★★ = 1개는 대입연산자

print(1 != 3) # 1과 3이 같지않다 True
print(not(1 != 3)) # 1과 3이 같지않다 의 반대 # False

print((3 > 0) and (3 < 5)) # 둘다 참일 때 True 출력
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 < 5)) # 하나라도 참일 때 True 출력
print((3 > 0) | (3 < 5)) # True

print(5 > 4 > 7) # 세 개 씩도가능
'''
#------------------------------------------------
'''
#2-2 간단한 수식
print(2 + 3 * 4) # 14
print((2+3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number += 2 # 16   연산 '*=','/=','%=','//=' 다 가능함
print(number)
'''
#--------------------------------
'''
#2-3 숫자 처리 함수
print(abs(-5)) # 5 절댓값출력
print(pow(4, 2)) # 16 제곱 4^2
print(max(5, 12)) # 12 더 큰 값 찾기
print(min(5, 12)) # 5 더 작은 값 찾기
print(round(3.14)) # 3 반올림
print(round(4.99)) # 5

from math import * # math 라이브러리 가져오기 중요!
print(fabs(-4.99))
print(floor(4.99)) # 4 내림
print(ceil(3.14)) # 4 올림
print(sqrt(16)) # 4 제곱근
'''
#---------------------------------------------
'''
#2-4랜덤함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
'''
#-----------------------------------------------
#2-5 QUIZ
# 코딩 스터디 모임
# 조건 1 : 랜덤날짜
# 조건 2 : 28일 이내로
# 조건 3 : 1~3일은 스터디 준비를 위해 제외
# 출력문 예제 "오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다."
from random import *
study = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월{0} 일로 선정되었습니다.".format(study))