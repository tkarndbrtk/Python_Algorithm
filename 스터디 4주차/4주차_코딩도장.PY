#Unit 13
'''
cost = int(input())
sale = input()
sale = sale.replace("Cash","")
num_sale = int(sale)
print(cost-num_sale)
'''
#----------------------
# Unit 14
'''
a,b,c,d = map(int,input().split())
if a>100 or b>100 or c>100 or d>100 or a<0 or b<0 or c<0 or d<0:
    print("잘못된 점수")
else:
    if (a+b+c+d)/4 >= 80:
        print("합격")
    else:
        print("불합격")
'''
# Unit 16
'''
a ='python'
for i in reversed('python'):
    print(i, end='')

x = int(input())
'''
'''
for i in range(1,10):
    y = x * i
    print(f"{x} * {i} ={y}")
'''
#Unit 17
'''
from random import*
dice = [(1,2,3),"홍지원 빠가",[1,2,3],"A",5*3] 
i = 0
while i !="A": # while 활용법
    i = choice(dice) # random함수의 choice 메소드 등장
    print(i)
while "hello": # 무한반복문
    print("a")

money = int(input())

while money>=1350:
    money-=1350
    print(money)
'''
#Unit 18
'''count = int(input('반복할 횟수를 입력하세요: '))
 
i = 0
while True:    # 무한 루프
    print(i)
    i += 1
    if i == count:    # i가 입력받은 값과 같을 때
        break         # 반복문을 끝냄
'''
'''
# 18장 마지막 심사문제 - 입력값 두 값 사이에 값을 출력하되, 끝자리가 3은 제외
start, stop = map(int, input().split())
 
i = start
 
while True:
    if i%10 ==3:
        i+=1
        continue
    if i>stop:
        break
    print(i, end=' ')
    i += 1
'''
#Unit 19 무한루프
'''
for i in range(5):
    for j in range(5):
        if j<(4-i):#               *
            print(" ", end="")#   **
        else: #                  ***
            print("*", end="")# ****
    print() #                  ***** 
'''
'''
x = int(input())
for i in range(x):
    for j in range(x*2-1): # i=0 일 때 x-1<=j<=x
        if x-i<= j+1 <=x+i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''
#Unit 20 공배수 FizzBuzz
'''
a,b = map(int,input().split())
for i in range(a,b+1):
    print("Fizz"*(i%5==0)+"Buzz"*(i%7==0) or i)
'''
#Unit 21 사각형그리기, 다각형, 원 그리기

import turtle as t
'''
t.shape('turtle')
t.color('red')
t.begin_fill()
for i in range(1000):
    t.forward(0.5)
    t.right(360/1000)
t.end_fill()
'''
n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')
for i in range(2*n):
    t.forward(line)
    if i%2==0:
        t.right(180-180/n)
    else:
        t.left(90-90/n)
t.mainloop()