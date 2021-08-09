#Unit 22 _ 리스트와 튜플 응용하기
'''
a = [1,2,3,4,5]
a.append(60) # [1,2,3,4,5,60] append는 끝에 요소 추가
print(len(a)) # 6   len은 리스트의 길이
a.append([60,70,80]) # 리스트 안에 리스트 추가하기
print(a) # [1, 2, 3, 4, 5, 60, [60, 70, 80]]
a.extend([60,70]) # extend는 리스트 확장하기
print(a) # [1, 2, 3, 4, 5, 60, [60, 70, 80], 60, 70]
a. insert(2,2.5) # insert는 원하는 인덱스에 요소 추가
print(a) # [1, 2, 2.5, 3, 4, 5, 60, [60, 70, 80], 60, 70]
a[1:1] = [1.1, 1.2] # a[x:x] 와 같이 시작인덱스 = 끝 인덱스 해주면 덮어쓰지않음
print(a) # [1, 1.1, 1.2, 2, 2.5, 3, 4, 5, 60, [60, 70, 80], 60, 70]
a.pop() # 아니까 패스
del a[0] # 아니까 패스
a.remove(1.1) # remove는 특정 값 제거 여러개면 처음 찾은 값 삭제
print(a.count(60)) # 2   count는 리스트 요소중 60의 개수 찾기
a.reverse() # reverse는 순서 뒤집기
a.sort() # sort는 정렬하기
a.clear # 요소 싹다 삭제
del a[:] # 이것도
'''
'''
b = [5,5,5,5,5]
c = b
print(c==b) # True    두 리스트의 요소가 완전히 같으면
print(c is b) # True  객체가 같다는 의미인건가?
b[2] = "ㅗ"
print(c) # [5, 5, 'ㅗ', 5, 5] b를 바꿨는데 c도 바뀌었네 ? 그럼 맞는 얘긴거지?

d = [5,5,5,5,5] 
e= d.copy()
print(e==d) # True          두 리스트의 요소가 완전히 같아도
print(e is d) # False       객채는 다를 수 있다.
d[2] = "ㅗ"
print(e) # [5, 5, 5, 5, 5]  d를 바꿨는데 불구하고 e는 안바뀌었네?

'''
'''
f = [2,20,200,2000,20000]
for i, j in enumerate(f): # enumerate(a, start=1) 하면 index 1부터 시작
    print(i,j)#           enumerate를 활용하여 index와 value값 동시에 출력하기
'''
# 리스트를 생성하는 다양한 방법
'''
h = [i for i in range(10)] # [식 for i in range(???)]
k = [i for i in range(10) if i%2 ==0]
print(h) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(k) # [0, 2, 4, 6, 8]
l = [i * j for j in range(2, 10) for i in range(1, 10)] # for문 두개 한줄에쓰기
print(l)
'''
# 리스트에 map 사용하기
'''
m= [1.2, 2.5, 3.7, 4.6]
m= list(map(int,m)) # int 자료형으로 변경
print(m)
n = list(map(str,range(10))) # str 자료형으로 0~9 만들기
print(n)
'''
# 튜플은?
'''
o = (i for i in range(10)) # 표현식에서 튜플선언안하고 괄호만 치면 제너레이러 표현식으로 인식
print(o) # <generator object (<genexpr> at 0x000001769FE2C4A0>
p = (38, 21 ,11 , 15, 40)
print(min(p)) # 11  이 외에도 max, sum 모두 사용 가능!
'''
# 심사문제 - 2의 거듭제곱 출력하기
'''
x,y = map(int,input().split())
z = list(2**i for i in range(x,y+1) )
z.pop(1)
z.pop(-2)
print(z)
'''
# Unit 23 2차원 리스트 사용하기
'''
a= [[1,2,3],[40],[500,600]]
print(a[2][0]) # 3행 첫번째인 500출력
a.append([]) # 톱니형 리스트를 생성하는 방법 *이걸 안하니까 추가가안됨
a[3].append(1000) #       1    2    3
a[3].append(2000) # a =  40
a[3].append(3000) #      500  600
a[3].append(4000) #      1000 2000 3000 4000
from pprint import pprint
pprint(a, indent=1, width=30) # 사각형 구조로 2차원 리스트출력하기
                              # indent는 들여쓰기 칸수, width는 가로폭

'''
'''
a = [[10,20],[30,40],[50,60]]
#배열 출력하는 다양한 방법
# 1.
for x, y in a:
    print(x,y)
# 2.
for i in a:
    for j in i:
        print(j, end=' ')
    print()
# 3.
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()
'''
'''
a = []

for i in range(3): # 바깥 리스트 3줄
    line = [] # 안쪽 리스트 빈리스트
    for j in range(2): # 안쪽리스트 개수 2개
        line.append(0) # 안쪽리스트 0 추가
    a.append(line) # 큰 리스트내 안쪽 리스트 추가
print(a) #[[0, 0], [0, 0], [0, 0]]
'''
'''
students = [
    ['호영', 'S', 26],
    ['규환', 'H', 25],
    ['경', 'Y', 21]
]
print(sorted(students, key=lambda student: student[1]))
# 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students, key=lambda student: student[2]))
# 안쪽 리스트의 인덱스 2를 기준으로 정렬
'''
'''
a = [[10, 20], [30, 40]]
import copy
b = copy.deepcopy(a) # 2차원 배열에서는 b = a.copy()는 b = a 와 같음
b[0][0] = 500        # 따라서 copy 모듈의 deepcopy 함수를 사용할 것 
print(a)             # [[10, 20],[30, 40]]
'''
# 코딩도장 23장 심사문제
'''
row, col = map(int,input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
    if len(matrix[i]) != col:
        print("가로 개수가 맞지 않습니다")
        break
matrix.append([])
for p in range(row): # 오류방지용 끝에 인덱스 1개씩 추가
    matrix[p].append(" ")
for o in range(col+1): # 오류방지용 제일 밑줄 리스트 추가
    matrix[row].append(" ")
for a in range(row):
    for b in range(col):
        if matrix[a][b] == '*': 
            print('*', end='') # 지뢰면 그대로 지뢰표시
        else:
            num = 0
            for k in range(a-1,a+2): #인근 지뢰 개수 찾기 
                for l in range(b-1,b+2):
                    if matrix[k][l] =='*':
                        num+=1
            print(num, end='')
    print()
'''
#Unit 24 문자열 응용하기
'''
# 문자열 바꾸기
a = 'Hello, My Name Is Hoyoung'
a= a.replace('Hello', 'goodbye')
print(a)
# 문자 바꾸기
table = str.maketrans('aeiou','12345') # a->1 e->2 i->3 o->4 u->5
print('apple'.translate(table)) # 1ppl2
# 문자열 분리
b= 'Hello, My Name Is Hoyoung'
b= b.split() # 문자열을 리스트로 바꾸기
print(b) # ['Hello,', 'My', 'Name', 'Is', 'Hoyoung']
# 문자열 합체
b= ' '.join(b)
print(b) # Hello, My Name Is Hoyoung
# 대문자, 소문자 , 왼쪽, 오른쪽 공백삭제하기
b= b.lower()
print(b)
b = b.upper()
print(b)
c = '        Hello, My Name Is Hoyoung        '
print(c)
c = c.lstrip() # 오른쪽은 .rstrip() 양쪽은 .strip()
print(c)
'''
# 서식 지정자
'''
print('%.2f'%3) # 3.00   %.숫자 --> 숫자에 따라 소수점생성 없으면 소수점6자리
print('%10s'%'안녕하세용') #     안녕하세용-->10칸짜리 만들고 오른쪽에 문자열정렬
'''
# 코딩도장 24-5 심사문제 단어수 세기
'''
import string
a = str(input())
a = a.split(' ')
for i in range(len(a)):
    a[i] = a[i].strip(string.punctuation)
print(a.count('the'))
'''
# Unit 25
'''
x = {'a' : 10, 'b' : 20, 'c' : 30}
# x.setdefault() 메소드 - key, value 지정
x.setdefault(1,20)
print(x) # {'a': 10, 'b': 20, 'c': 30, 'e': 20}

# x.update() 메소드 - key 수정
x.update(a = 100) 
print(x) # {'a': 100, 'b': 20, 'c': 30, 'e': 20}

# update와 setdefault의 차이가 뭘까??
x.update(f=None,g=None)
print(x) # {'a': 100, 'b': 20, 'c': 30, 1: 20, 'f': None, 'g': None}
# key가 숫자일 때 update는 사전 지정할 때 처럼 해야 한다.
x.update({20: 'a'}) 
print(x) # {'a': 100, 'b': 20, 'c': 30, 1: 20, 'f': None, 'g': None, 20: 'a'}

# pop() 메소드 - 특정 key 삭제
x.pop(1) 
print(x) # {'a': 100, 'b': 20, 'c': 30, 'f': None, 'g': None, 20: 'a'}
# popitem() 메소드 - 제일 마지막 key 삭제
x.popitem()
print(x) # {'a': 100, 'b': 20, 'c': 30, 'f': None, 'g': None}
# clear 
x.clear() # 다 삭제
print(x) # {}

x = {'a' : 10, 'b' : 20, 'c' : 30}

# x.get() 메소드 - value값 가져오기
print(x.get('b')) # 20    
# x.items() 메소드 - 요소 다 가져오기
print(x.items()) # dict_items([('a', 10), ('b', 20), ('c', 30)])
# x.keys() 메소드 - key값 다 가져오기
print(x.keys()) # dict_keys(['a', 'b', 'c'])
# x.values() 메소드 - value값 다 가져오기
print(x.values()) # dict_values([10, 20, 30])

# 리스트와 튜플로 딕셔너리 만들어보기
keys = ['파이썬', '기획세미나', 'Figma', '이엠 축구', '운티미회의']
values = ('목,수','토','화','월','수')
# zip 활용하면 리스트 튜플을 묶어서 만들 수 있음!
x = dict(zip(keys,values))
print(x) #{'파이썬': '목,수', '기획세미나': '토', 'Figma': '화', '이엠 축구': '월', '운티미회의': '수'}
# for 반복문을 이용해 만들기
y = {key: value for key, value in dict.fromkeys(keys).items()}
print(y) #{'파이썬': None, '기획세미나': None, 'Figma': None, '이엠 축구': None, '운티미회의': None}

# 반복문으로 모든 key, value 출력
for key, value in x.items():
    print(key,value)

# 딕셔너리에서 for 반복문으로 key,value를 삭제하려고 하면 오류가 발생
# 대신에 새로운 딕셔너리를 지정하면서 삭제해야함
x = {key : value for key, value in x.items() if value !='토'} # 기획세미나삭제
print(x) # {'파이썬': '목,수', 'Figma': '화', '이엠 축구': '월', '운티미회의': '수'}
'''
# 중첩 딕셔너리
'''
planet = {
    '수성' : {
        '평균 반지름' : 2439.7,
        '질량' : 3.3022E+23,
        '공전주기' : 87.969
    },
    '금성' : {
        '평균 반지름' : 6851.8,
        '질량' : 4.8676E+24,
        '공전주기' : 224.70069
    },
    '지구' : {
        '평균 반지름' : 6371.0,
        '질량' : 5.97219E+24,
        '공전주기' : 365.25641
    },
    '화성' : {
        '평균 반지름' : 3389.5,
        '질량' : 6.4185E+23,
        '공전주기' : 686.9600
    }
}
print(planet)
'''
# 딕셔너리 할당과 복사는 리스트와 동일하다
'''
x = {'a' : 10, 'b' : 20}
y = x
x.update(a= 50)
print(y is x)
print(y)        # 리스트처럼 x업데이트하면 y도 바뀜 ==> 객체가 아예 같음
                # 즉, y==x 가 아닌 y= x.copy()를 이용해야 객체가 달라짐
                # 중첩의 경우 리스트와 마찬가지라 import copy 모듈의
                # copy.deepcopy(x) 사용할 것.remove('Python')
'''
# 25장 심사문제
'''
keys = input().split()
values = map(int, input().split())
 
x = dict(zip(keys, values))

x = {key : value for key, value in x.items() if value !=30}
x = {key : value for key, value in x.items() if key !='delta'}

print(x)
'''
# Unit 26
'''
a = {1,2,3,4,5}
# print(a[3]) # Error 세트는 순서에 따른 인덱스 뽑기가 불가능.
print('바보' in a) # False 요소의 존재 여부는 확인 가능

b = set('야 이 똥멍청아')

print(b) # {'멍', '야', '청', '이', '아', ' ', '똥'}
# 보다시피 띄어쓰기가 두개임에도 불구하고 하나만 나옴 --> 중복X
# Set 안에 Set를 넣을 수 없음
# 요소를 변경할 수 없는 frozenset가 존재
c = frozenset({frozenset({1,2}),frozenset({3,4})})
# frozenset({frozenset({3, 4}), frozenset({1, 2})})
print(c)
'''

A = {1,2,3,4}
B = {1,2,5,6,7}

print(A|B) # {1, 2, 3, 4, 5, 6, 7} 합집합
print(A&B) # {1, 2} 교집합
print(A-B) # {3, 4} 차집합
print(A^B) # {3, 4, 5, 6, 7} 전체-교집합
A |= {5} # A와 5의 합집합 --> 5라는 요소 추가
print(A) # {1, 2, 3, 4, 5}
A-={5} # A와 5의 차집합 --> 5 삭제
print(A) # {1, 2, 3, 4}
A &= B # A는 A와 B의 교집합
print(A) # {1, 2}
# 상위 집합 인지 확인하기
print(B>={1,2}) # True
print(B>={1,2,3}) # False
# 겹치는지 확인하기
print(B.isdisjoint({5,9,0,11})) # 겹치는 요소가 있으면 False

# 요소 추가
A.add('기') # |= 와 같은 효과
print(A) # {1, 2, '기'}
# 요소 제거 ( 에러발생 ) 있으면 제거, 없으면 에러
A.remove(1) # -= 와 같은 효과
# 요소 제거 ( 에러생략) 있으면 제거, 없으면 그냥 진행
A.discard(1)
print(A) # {2, '기'}
# 임의 요소 제거
print(A.pop())
print(A) # {'기'}
# 모든 요소 제가
A.clear()
print(A) # set()

# 26장 심사문제
'''
x, y = map(int,input().split())
a = {int(x/i) for i in range(1,x+1) if x%i ==0 }
b = {int(y/i) for i in range(1,y+1) if y%i ==0 }
print(a)
print(b)
'''
