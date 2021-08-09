# 5-1 리스트

# 지하철 칸별로 10, 20, 30명

# 지하철1 = 10
# 지하철2 = 20
# 지하철3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["장경환","박윤상","정인혁"]

# #이뇨기가 몇번째칸?
# print(subway.index("정인혁"))

# subway.append("이준호")
# print(subway)
# subway.insert(1, "유진호")
# print(subway)
# subway.append("장경환")
# print(subway.count("유재석"))


# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

#다양한 자료형과 함께사용
# num_list = [5,2,4,3,1]
# mix_list = ["서호영", 20, True]
# print(mix_list)
# #리스트확장
# num_list.extend(mix_list)
# print(num_list)
#-------------------------------------------------------------------
#5-2 사전
# cabinet = {3:"서호영", 100:"장하은","A-3":"정인혁","B-100":"지솔"}
# # print(cabinet[3])
# # print(cabinet[100])
# # print(cabinet.get(3))
# # print(cabinet.get(5))
# # print("hi")
# print(3 in cabinet)
# print(5 in cabinet)

# print(cabinet["A-3"])
# print(cabinet["B-100"])
# print(cabinet)
# cabinet["C-20"] = "최인수"
# cabinet["A-3"] = "장경환"
# print(cabinet)

# #손님 나감
# del cabinet["A-3"]
# print(cabinet)

# # key만 출력
# print(cabinet.keys())

# # value값만 출력
# print(cabinet.values())

# # key랑 value 둘다
# print(cabinet.items())

# # 모든 값 제거
# cabinet.clear()
# print(cabinet)
#--------------------------------------------------------------------
#5-3 튜플
# menu = ("연어", "광어")
# print(menu[0])
# print(menu[1])

# #추가는 불가

# # name = "서호영"
# # age = 20
# # hobby "코딩"
# # print(name, age, hobby) --> 튜플로

# (name, age, hobby) = ("서호영", 20, "코딩")
# --------------------------------------------------------------------
# 집합 (set)
# 중복 x, 순서 x
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"서호영", "장경환", "김승모"}
# python = set(["서호영", "정인혁"])

# #교집합
# print(java & python)
# print(java.intersection(python))

# # 합집합 (java 또는 python 하나라도 할 수 있는 사람)
# print(java| python)
# print(java.union(python))

# # 차집합 (자바 가능 but 파이썬 불가능한 사람)
# print(java-python)
# print(java.difference(python))

# # 파이썬 할 줄 아는 사람이 늘어남
# python.add("김승모")
# print(python)

# # 자바를 까먹음
# java.remove("서호영")
# -------------------------------------------------------------------
# 자료구조의 변경
# 커피숍
# menu = {"라떼","자몽티","밀크티"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))