'''
#3-1 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬 is so EZ"
print(sentence2)
sentence3="""
나는 소년이고
파이썬 is so EZ
- 홍지원
"""
print(sentence3)
'''
#-------------------------------
'''
#3-2 슬라이싱 - 필요한 만큼만 가져오기
jumin = "961013-1234567"

print("성별 : " + jumin[7])
print("년 : " + jumin[:2]) # 처음부터 1번째 글자까지 출력
print("월 : " + jumin[2:4]) # 3번째 ~ 4번째 글자 출력
print("일 : " + jumin[4:6]) # 5번째 ~ 6번째
print("생년월일 : " + jumin[:6]) # 처음 ~ 6번째
print("뒤 7자리 : " + jumin[7:]) # 8번째 ~ 끝까지
print("뒤 7자리 : " + jumin[-7:]) # 끝에서 7번째 ~ 끝
'''
#----------------------------------------------
'''
#3-3 문자열 처리 함수
python = "Python is so Ez - Python"
print(python.lower()) # 다 소문자로
print(python.upper()) # 다 대문자로
print(python[0].isupper()) # 첫번째가 대문자야? 참 거짓
print(len(python)) # 문자열 길이
print(python.replace("Python", "Java")) # 해당 글자 모두 대체

index = python.index("n") # 5 n이 위치한 곳
print(index)
index = python.index("n", index + 1) # 그 다음부터 n위치한 곳
print(index)
print(python.find("Java")) # -1 존재하지 않을 때 .index를 이용하면 오류, find를 이용하면 -1 반환
print(python.count("n"))
'''
#------------------------------------------------
'''
#3-4 문자열 포멧
print("나는 %d살 입니다." % 20) # 나는 20살입니다. - 정수값 대입가능
print("나는 %s을 좋아해요." % "파이썬") # 나는 파이썬를 좋아해요 - 문자열 대입가능
print("나는 %c을 좋아해요." % "A") # 나는 A를 좋아해요 - 문자 대입가능
# 그냥 %s로 쓰면 다 출력가능
print("나는 {}살입니다.".format(20)) # 나는 20살입니다.
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간")) # 나는 파란색과 빨간색을 좋아해요.
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간")) # 나는 파란색과 빨간색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간")) # 나는 빨간색과 파란색을 좋아해요.

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간")) # 나는 20살이며, 빨간색을 좋아해요.
age = 20
color = "벌건"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # 나는 20살이며, 벌건색을 좋아해요.
'''
#---------------------------------------------------------
'''
#3-5 탈출문자
print("백문이 불여일견\n백견이 불여일타") # \n을 통한 줄바꾸기
print("저는 '나도코딩' 입니다.") # 출력문 내에 """" 반복사용은 불가
print("저는 \"나도코딩\" 입니다.") # 사용할거면 탈출문자인 \를 이용할 것
print("C:\\Users\\user\\Desktop\\Python WorkSpace")# \\ : 문장 내의 \역할
print("Red Apple\rPine")#\r : 커서를 맨 앞으로 이동
#\b : 백스페이스 (한 글자 삭제)
#\t : 탭의 역할
'''
#---------------------------------------------------------
'''
# 3-6 Quiz
# 사이트별 비밀번호 만들어주는 프로그램 작성
# 규칙 1 : http://naver.com 중 http:// 제외
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 =>naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로구성

url = "http://naver.com"
url_1 = url.replace("http://","") # 규칙 1 적용
url_2 = url_1[:url_1.index(".")] # 규칙 2 적용
key = url_2[:3] + str(len(url_2)) + str(url_2.count('e')) + '!' # 규칙 3 적용
print(" 아이디 {0} 의 비밀번호 : {1}".format(url,key))
# 아이디 http://naver.com 의 비밀번호 : nav51!
'''