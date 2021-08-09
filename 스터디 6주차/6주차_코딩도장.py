# Unit 27 파일사용하기
# # 파일쓰기
'''
file = open('hello.txt','w')
file.write('Hello world!')
file.close()
'''
# 파일 읽기
'''
file = open('hello.txt','r')
s = file.read()
print(s)
file.close()
'''
# 파일과 리스트
# 자동으로 파일 객체 닫는법 - with open() as file: 사용하기
'''
wlines = ['안녕하세요\n','제 이름은\n','호빡이입니다 :)\n']
rlines = []
with open('hello.txt','w') as file:
    file.writelines(wlines)
with open('hello.txt','r') as file:
    file.readlines(rlines)
    print(rlines)
'''
# while문으로 만들기
'''
with open('hello.txt','r') as file:
    line = None
    while line !='':
        line = file.readline()
        print(line.strip('\n'))
    rlines = file.readlines() # 고찰:    앞에 읽어버리면 그 다음에 써도
    print(rlines)             # []      처음부터 읽혀지지 않는다.

# for문으로 만들기
with open('hello.txt','r') as file:
    for line in file:
        print(line.strip('\n'))
# 파이썬 객체 파일에 저장하기, 가져오기 
# 피클링과 언피클링
import pickle
name = 'ho_aeng'
age = 26
address = '서울시 노원구 월계동'
scores = {'python' : 90, 'javascript' : 95, 'C':70, 'C#' : 82}

with open('ho_aeng.p','wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

    
with open('ho_aeng.p','rb') as file:
    r_name = pickle.load(file)
    r_age = pickle.load(file)
    r_address = pickle.load(file)
    r_scores = pickle.load(file)
    print(r_name)
    print(r_age)
    print(r_address)
    print(r_scores)
'''
# Unit 27 심사문제
# words.txt 파일 주어짐 ,로 이루어진 긴 문장임.
'''
import string
with open('words.txt','r') as file:
    b = file.readlines()
    b = str(b)                            # 문자열로 치환한 이유는?
    b = b.split()
    for i in range(len(b)):
        b[i] = b[i].strip(string.punctuation)
        if 'c' in b[i]:
            print(b[i])
'''
#-----------------------------------------
# Unit 28 회문 판별하기

# 방법 1
'''
word = input('단어를 입력하세요: ')
 
is_palindrome = True                 # 회문 판별값을 저장할 변수, 초깃값은 True
for i in range(len(word) // 2):      # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 - i]:      # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        is_palindrome = False        # 회문이 아님
        break
 
print(is_palindrome)                 # 회문 판별값 출력
'''
# 방법 2
'''
word = input('단어를 입력하세요: ')
print(word == word[::-1])    # 원래 문자열과 반대로 뒤집은 문자열을 비교
'''
# 방법 3
'''
word = input('단어를 입력하세요: ')
print(list(word) == list(reversed(word)))
'''
'''
a = 'hello'
two = zip(a,a[1:])
print(two)
'''