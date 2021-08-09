'''
#4-1 리스트
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway) # [10, 20 ,30]

subway = ["유재석", "조세호", "박명수"]
print(subway) # ['유재석', '조세호', '박명수']

# 조세호는 몇 번째 칸에?
print(subway.index("조세호")) # 2

#하하가 다음 정류장에서 탔다.
subway.append("하하")
print(subway) # ['유재석', '조세호', '박명수', '하하']

#정형돈을 유재석/ 조세호 사이에 태웠음.
subway.insert(1, "정형돈")
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']

# 지하철에 있는 사람을 꺼낸다.
print(subway.pop()) #하하
print(subway) #['유재석', '정형돈', '조세호', '박명수']


print(subway.pop()) # 박명수
print(subway) # ['유재석', '정형돈', '조세호']

print(subway.pop()) # 조세호
print(subway) # ['유재석', '정형돈']

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]


#뒤집기 가능
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

#모두지우기
num_list.clear()
print(num_list) # []

#다양한 자료형 함께 사용 가능
mix_list = ["서호영", 20, True]

#리스트 확장
num_list.extend(mix_list)
print(num_list) # ['서호영', 20, True]

'''
#------------------------------------------------------------
'''
#4-2 사전(dictionary)
cabinet = {3:"유재석", 100:"김태호"}

print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

print(cabinet.get(3))
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

# 새 손님
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}

cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"]
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}

#key 만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

#value 만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])

#key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 폐점
cabinet.clear()
print(cabinet)
'''
#-------------------------------------------------------
'''
#4-3 튜플
menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

# menu.add("생선까스") 불가능

name ="김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
'''
#------------------------------------------------------------
'''
#4-4 세트
# 중복 x ,순서 x
my_set= {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 찾기
print(java & python) #{'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 찾기
print(java|python) # {'유재석', '박명수', '김태호', '양세형'}
print(java.union(python)) # {'유재석', '박명수', '김태호', '양세형'}

# 차집합
print(java - python) # {'김태호', '양세형'}
print(java.difference(python)) # {'김태호', '양세형'}

#python 한명 추가
python.add("김태호")
print(python) # {'김태호', '유재석', '박명수'}
'''
#--------------------------------------------------
'''
# 4-5 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # {'우유', '주스', '커피'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['우유', '주스', '커피'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('우유', '주스', '커피') <class 'tuple'>
'''
#---------------------------------------------------------
# 4-6 Quiz
# 댓글작성자 중 1명 치킨, 3명 커피쿠폰
# 작성자는 20명 아이디는 1~20
# 무작위 추첨, 중복불가
# random 모듈의 shuffle 과 sample 활용

from random import *

lotto = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(lotto)

print("----- 당첨자 발표 -----")

chicken = lotto[0]
del lotto[0]
print("치킨 당첨자 : {0}".format(chicken))
print("커피 당첨자 : {0}".format(sample(lotto, 3)))
print("----- 축하합니다 -----")