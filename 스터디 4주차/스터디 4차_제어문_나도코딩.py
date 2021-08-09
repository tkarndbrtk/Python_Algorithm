#5-1 if
'''
weather = input("오늘 날씨 어때?")
if weather =="비" or "눈" :
    print("우산을 챙기시오")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))
if temp >=30:
    print("더워요, 나가지 마세요")
elif 30> temp >= 10 :
    print("괜찮은 날씨요")
elif 10>temp>=0:
    print("외투를 챙겨요")
else:
    print("너무 추워, 나가지마세요")
'''
#----------------------------------
#5-2 for
'''
for waiting_no in [0, 1, 2, 3, 4] :
    print(f"대기번호 : {waiting_no}")

starbucks = ["지원","호영","동진","규환","효리"]
for customer in starbucks:
    print(f"{customer}, 커피가 준비되었습니다")
'''
#----------------------------
#5-3 while
'''
customer = "지원"
index = 1
while index>=1:
    print(f"{customer}손님, 커피가 준비되었습니다. 남은 호출 횟수{index}번")
    index -=1
    if index ==0:
        print("커피가 폐기되었습니다.")

customer = "동진"
person = "Unknown"

while person != customer :
    print(f"{customer}님, 커피가 준비되었습니다.")
    person = input("성함이 어떻게 되세요? ")
'''
#--------------------------------
#5-4 continue, break
'''
absent = [2, 5] # 결석자 출석번호
no_book =[7] # 책 없는놈
for student in range(1,11): # 1~10번
    if student in absent:
        continue # 헷갈림주의
    elif student in no_book:
        print(f"오늘 수업 여기까지 {no_book}번은 교무실로 따라와")
        break 
    print(f"{student}번, 책 읽으세요")
'''
#---------------------------------
#5-5 한줄 for문
'''
students = [1,2,3,4,5]
print(students) # [1, 2, 3, 4, 5]
students = [i+100 for i in students]
print(students) # [101, 102, 103, 104, 105]

# 학생 이름을 기링로 변환
students =["Iron man","Thor", "I am groot"]
students = [len(i) for i in students]
print(students) #[8, 4, 10]

# 학생 이름을 대문자로 변환
students =["Iron man","Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)
'''
#-------------------------------------
# 5-6 Quiz 6
'''
from random import*
num = 0 # 제일 마지막 총 탑승 승객 수를 나타낼 변수
for i in range(1,51): # 50명의 승객
    x = randint(5,50) # 5~ 50분
    if x<=15: # 15분 이하일 때 
        A="O" # 앞에 O표시
        num += 1 # 동시에 탑승 승객수 증가
    else: 
        A="" # 아니면 빈칸
    print(f"[{A}] {i}번째 손님 (소요시간 : {x}분 )")
print(f"총 탑승 승객 : {num} 분")
'''