#6-2 전달값과 반환값
"""
def open_accont():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): #입금
    print(f"입금이 완료되었습니다. 잔액은 {balance + money}원 입니다.")
    return balance + money # 질문 : 여기서 return에 balance+money를 넣어주는 이유는?

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액 > 출금액
        print(f"출금이 완료되었습니다. 잔액은 {balance-money} 원 입니다.")
        return balance-money
    else:
        print(f"출금이 되지 않았습니다. 잔액은 {balance}원 입니다.")
        return balance
def withdraw_night(balance, money): # 저녁 출금
    commission = 100 # 수수료
    return commission, balance - money - commission
balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print(f"수수료 {commission}원 이고, 잔액은 {balance}원 입니다.")
"""

#6-3 기본값
'''
def profile(name, age, main_lang):
    print(f"이름 : {name}\t나이 :{age}\t주 사용 언어: {main_lang}")
    # 기본값 설정하기
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

#같은 학년 같은 반일 때 
def profile(name, age=17, main_lang="파이썬"):
     print(f"이름 : {name}\t나이 :{age}\t주 사용 언어: {main_lang}")

profile("유재석")
profile("김태호")
'''

#6-4 키워드
'''
def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(main_lang="자바", age=25, name="김태호")
profile(name="유재석",main_lang="파이썬",age=20) # 매개변수 값으로 
'''
#6-5 가변인자
'''
#def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#   print(f"이름 : {name}\t나이 : {age}\t", end =" ") # 우리는 너무나도 잘 아는 end 의 개념
#   print(lang1,lang2,lang3,lang3,lang4,lang5)

def profile(name, age, *language): # 가변인자 * 를 이용하자!
    print(f"이름 : {name}\t나이 : {age}\t", end =" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C","C++","C#")
profile("유재석", 20, "Swift", "Kotlin")
'''

#6-6 지역변수와 전역변수
'''
gun = 10 #총 10자루

def checkpoint(soldiers): # 경계근무
    global gun # ※ 전역 공간에 있는 gun 사용 ※
    gun = gun - soldiers
    print(f"[함수 내] 남은 총 : {gun}")

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers # 전역 공간의 gun을(global) 사용하지 않고 하는 법
    print(f"[함수 내] 남은 총 : {gun}")
    return gun

print(f"전체 총 : {gun}")
#checkpoint(2) # 경계근무 2명나감
gun = checkpoint_ret(gun, 2)
print(f"남은 총 : {gun}")
'''
#6-7 퀴즈

# 표준체중 구하는 프로그램 작성
# 남자 : 키(m)^2 * 22
# 여자 : 키(m)^2 * 21
# 함수명 : std_weight , 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

def std_weight(height, gender):
    m_weight = round((height**2)*22,2)
    w_weight = round((height**2)*21,2)
    if gender =="남자":
        print(f"키 {height*100}cm 남자의 표준 체중은 {m_weight}입니다.")
        return m_weight
    elif gender =="여자":
        print(f"키 {height*100}cm 여자의 표준 체중은 {w_weight}입니다.")   
        return w_weight
        

std_weight(1.70, "남자")