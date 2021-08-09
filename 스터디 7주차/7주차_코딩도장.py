# Unit 29 함수 사용하기

'''
def a(b):
    """이거슨 바로 독스트링"""
    return 20

def not_hundred(a):
    if a==100:
        return
    print(f"{a}입니다")

not_hundred(200) # 200입니다
not_hundred(100) #

def not_two():
    return 1, 5

x = not_two()
print(x,type(x)) # (1,5) <class 'tuple>
# 이게 튜플형식으로 바뀐다!!!! 오우오우...

def mul(a, b):
    c = a-b
    return c
def add(a, b):
    c = a+b
    print(c) # 15
    d = mul(a, b)
    print(d) # 5
    print(c) # 몇일까요? 여러분들? 

x = 10
y = 5
add(x, y)

def calc(x,y):
    a = x+y
    s = x-y
    m = x*y
    d = x/y
    return a, s, m, d

'''
# Unit 30 함수에서 위치인수와 키워드인수 사용하기
'''
def num(a, b, c):
    print(a)
    print(b)
    print(c)
x = [10, 20, 30]
num(*x) # 오류 -> 함수의 매개변수 개수와 리스트의 요소 개수가 같아야한다.

# 이러한 문제를 해결하는 방법!
def num_sol(*ys):
    for y in ys:
        print(y)

num_sol(10, 20, 30, 40, 50) # 10
                            # 20
                            # 30
                            # 40
                            # 50


# 키워드 인수로 순서를 안 외워도 되게끔!
def keyword(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
keyword(age= 22, address= "분당구 야탑동", name = "서호빡" )

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)# value 값이 출력
personal_info(*x) # key 값이 출력

def personal_dic(**kwargs):
    for kw, arg in kwargs.items(): # items() 를 사용하여 key와 value값을 두 변수에 할당
        print(kw, ': ', arg, sep='')

personal_dic(**x)

def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('서호영', 26) # 초기값이 뒤에있기 때문에 오류x
def personal_error(name, age= 26, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

# unit 30 심사문제

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    return min(args), max(args)
def get_average(**args):
    return sum(args.values())/len(args)
min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
'''

# Unit 31 재귀호출 사용하기
'''
def hello(x):
    if x==0:
        return
    print('Hello, world!')
    x-=1
    hello(x)
 
hello(5) # 5번 재귀호출

def fac(n):
    if n==1:
        return 1
    return n * fac(n-1) # 역으로 다시 올라간다는 개념이 매우 어려웠음.
# 회문판별 재귀함수 만들기
def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])
# 소ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ름

# unit31 심사문제
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1) + fib(n-2)
n = int(input())
print(fib(n))
'''
# Unit 32 람다 표현식으로 함수 만들기
'''
plus_10 = lambda x: x+10 # 새로운 개념 람다함수의 등장
print((lambda x: x+10)(1)) # 11  람다함수 자체를 호출
print(plus_10(1)) # 11
# ※ 람다 표현식 내에서는 변수선언이 불가능함. 대신 바깥변수는 사용가능
# map에 대해서 공부해보자.
def plus_10(x): # 10을 더해주는 함수를 만들어 보았다.
    return x+10
def plus_9(x): # return에 람다식을 이용해 함수를 만들었다.
    return lambda x: x+9
def plus_pick(n): # 변수를 함수로 만들 수 있는 람다수를 함수로 만들었다.
    return lambda x: x+n
plus_7 = plus_pick(7)
print(plus_7(10)) # 17  좀 이해하기 어려웠다.
a = list(map(plus_10, [1, 2, 3])) # 리스트를 map을 이용해 함수에 넣어 값 출력
print(a) # [11, 12, 13]

b = list(map(lambda x: x + 10, [1, 2, 3])) # 위와 같은걸 람다식으로 표현
print(b) # [11, 12, 13]

# 자, 그러면 람다표현식을 왜 사용할까? 이상하기만 한데?

# 람다 표현식 함수는 익명 함수이기 때문에 사용하고 난 후에 
# 힙 메모리 영역에서 사라지기 때문에 단발성으로 사용하기에 편하고 좋다.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(map(lambda x: str(x) if x % 3 == 0 else x, a)) # lambda식에서는 if를 사용시 반드시 else를 사용해야함
print(a) # 3의 배수를 문자열로 바꾸는 조건식

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
# x가 1이면 문자열, 2이면 실수로, 나머지는 10을 더하는 조건식
# 람다로 이런 표현을 하면 조금 복잡하다.

def f(x):           # 그럴빠에 이렇게 하자.
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10

# map을 이용할 때, 객체를 여러개 넣을 수 있다!

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
a_multi_b= list(map(lambda x, y: x * y, a, b))
print(a_multi_b) # [2, 8, 18, 32, 50]

def g(x,y):
    return x+y
def f(x):
    return 5 < x < 10 # True 또는 False 출력하는 Boolean함수

a= [10, 4, 7, 6, 11, 6.5, 8.2]

print(f(4)) # False

a = list(filter(f,a)) # True인 요소만 걸러주는 친구 filter
print(a) # [7, 6, 6.5, 8.2]
from functools import reduce

print(f(1)) # ※ 실행이 될까?

b = [1, 2, 3, 4, 5]
print(reduce(g,b)) # 15

# 사진파일 필터링
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

a = list(filter(lambda x: '.jpg' in x or '.png' in x,files))
print(a)

# 심사문제

files = input().split()

print(list(map(lambda x:'00'+x if len(x[0:x.find('.')]) == 1 
                    else '0'+x  if len(x[0:x.find('.')])==2 else x, files)))
'''
# Unit 33 클로저 사용하기
'''
x = 10
def foo():
    print(x)

foo()
print(x)

# 전역함수의 변수를 안쪽 함수에서 사용할 수 있다. 수정하려면 nonlocal을 쓰자.

def A():
    x = 10        # A의 지역 변수 x
    def B():
        nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20        # A의 지역 변수 x에 20 할당
 
    B()
    print(x)      # A의 지역 변수 x 출력
 
A()
# 전역함수 안의 x와 해당함수 안의 x 그리고 그 함수 안에서
# nonlocal로 지역변수를 가져올 때, 바로 바깥 함수에 있는 x부터 가져온다
# global을 사용하면 무조건 전역변수를 사용하게 됨.

# 클로저 개념
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환
 
c = calc()
print(c(1), c(2), c(3), c(4), c(5))

# 심사문제
def countdown(n):
    def a():
        nonlocal n
        n-=1
        return n+1
    return a    

n = int(input())
 
c = countdown(n)
for i in range(n):
    print(c(), end=' ')
'''