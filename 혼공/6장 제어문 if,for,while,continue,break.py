#6장

# 6-1 if문

# #weather = "???"
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather =="눈":
#     print("우산을 챙기세연")
# elif weather =="미세먼지":
#     print("마스크릉 챙기세연")
# else:
#     print("준비물 필요없어 연")

# temperature = int(input("기온이 어때요?"))
# if 30<= temperature:
#     print("개더워 나가지 마세연")
# elif 10<=temperature <= 30 :
#     print("얼른 밖에 나가세연~ 좋은 날씨에요")
# elif 0<= temperature < 10:
#     print("살짝 추워연 외투를 챙겨가세요")
# else:
#     print("얼어디쟈요 나가지마세연")
#---------------------------------------------------------------------

# 6-2 for문 

# print("대기번호 : 0")
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# # randrange()
# for waiting_no in range(1,6): #0, 1, 2, 3, 4
#     print("대기번호 : {0}".format(waitin g_no))

# starbucks = ["아이언맨","토르","머쉬베놈"]
# for customer in starbucks:
# print("{0}님, 커피 나왔습니다!".format(customer))
#----------------------------------------------------------------------------
# 6-3 while문
# customer = "토르"
# index = 5
# while index >=1:
#     print("{0}, 카피가 준비되었습니다. {1} 번 남았어요.".format(customer,index))
#     index-=1
#     if i ==0:
#         print("커피가 폐기처분되었습니다.")
# customer="아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer,index))
#     index +=1
# customer="토르"
# person = "Unknown"

# while person!= customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("성함이 어떻게 되세요??")
#-------------------------------------------------------------------------
#6-4 continue 와 break
# absent = [2, 5] #결석자
# no_book = [7] # 책을 깜빡함
# for student in range(1,11):
#     if student in absent:
#         continue # 다음반복으로 바로 넘어가도록 하는 실행문
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))
#--------------------------------------------------------------
# 6-5 한줄 for문

students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "Mushbanom"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Mushbanom"]
students = [i.upper() for i in students]
print(students)