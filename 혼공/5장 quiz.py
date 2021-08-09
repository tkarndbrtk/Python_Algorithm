# # Quiz) 파이썬 코딩대회 주최
# 댓글이벤트 진행
# 댓글작성자들 중 추첨을 통해 1명치킨 3멍은 커피쿠폰
# 추첨프로그램 작성

# 조건1 : 댓글은 20명이 작성, 아이디는 1~20 가정
# 조건2 : 댓글 내용무관 무작위 추첨 but 중복불가
# 조건3 : random 모듈의 shuffle과 sample활용

# 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

#활용 예제
# from random import *
# print(lst)
# shuffle(lst)
# print(lst)
from random import *
users = range(1,21) #lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
users = list(users)
print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명중 1명은 치킨 3명은 커피
#-------------------------------------------
# print("-- 당첨자 발표 --")
# print('치킨 당첨자 :' + sample(users,1))
# print('커피 당첨자 :' + sample(users,3))
# print("-- 축하합니다 --")  왜안돼 ?????????????????
#--------------------------------------------
print("--  당첨자 발표 --")
print('치킨 당첨자 : {0}'.format(winners[0]))
print('커피 당첨자 : {0}'.format(winners[1:]))
print("-- 축하합니다 ! --")