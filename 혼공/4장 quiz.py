# 비밀번호 만들기  http://naver.com 의 비밀번호
# 규칙1 : http:// 부분 제외
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외한다
# 규칙3 : 남은 글자 중 처ㅡㅁ 세자리 + 글자 개수 + 글자 내 'e' 개수 + "1"로 구성

url = "http://naver.com"
rule1 = url.replace("http://","")
print(rule1)
rule2 = rule1[:rule1.index(".")]
print(rule2)
password = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + "!"
print(password)

print("{0}의 비밀번호는 {1}이다.".format(url,password))