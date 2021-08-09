### 그리디 ###

#1. 거스름 돈 문제
'''
x = int(input())
N = 0
while 1:
    if x>=500:
        N = x//500
        x%=500
    elif 500>x>=100:
        N+=(x//100)
        x%=100
    elif 100>x>=50:
        N+=(x//50)
        x%=50
    elif 50>x>=10:
        N+=(x//10)
        x%=10
    else:
        break
print(N)
'''
#2. 1이 될 때까지
'''
n, k = map(int,input().split())
cnt = 0
while 1:
    if n==1:
        break
    elif n % k==0:
        n/=k
    else:
        n-=1
    cnt+=1
print(cnt)
'''
#3. 곱하기 혹은 더하기
'''
n = input()
lst = list(map(int,str(n)))
result = 0
for i in lst:
    if i > 1 and result > 1:
        result *= i
    else:
        result+=i
print(result)
'''
#4. 모험가 길드
'''
p_num = int(input())
lst = list(map(int,input().split()))
group = 0
cnt = 0
for i in range(1, len(lst)+1):
    cnt+= lst.count(i)
    group += cnt//i
    cnt = lst.count(i) % i
print(group)
'''
### 구현 ###
#문제 1. 상하좌우
'''
ran = int(input())
lst = list(input().split())
x, y = 1, 1
for i in lst:
    if i =='R' and y<ran:
        y+=1
    elif i =='L'and y>1:
        y-=1
    elif i =='D'and x<ran:
        x+=1
    elif i =='U'and x>1:
        x-=1
print(x,y)
'''
# ------------------정석풀이----------------------
'''
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
'''
#-----------------------------------------
#문제2. 시각
'''
N = int(input())
cnt = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if i//10 ==3 or i%10 == 3 \
                or j//10 ==3 or j%10 ==3 \
                or k//10 ==3 or k%10 ==3:
                    cnt += 1

print(cnt)
'''
# 문제3. 왕실의 나이트
# a의 아스키코드 97 ord('a')
'''
2 , 2 : 8
2 , 1 : 6
2 , 0 : 4
1 , 1 : 4
1 , 0 : 3
0 , 0 : 2
'''
'''
Pos = list(map(str,input()))
cnt = 0
move = [(2, 1),(2, -1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
x, y = int(ord(Pos[0])-96) , int(Pos[1])

for i in move:
    if 8>= x+i[0] >=1 and 8>=y+i[1]>=1:
       cnt+=1
print(cnt)
'''
#문제4. 문자열 재정렬
'''
x = list(input())
x.sort()
y = ''
sum = 0
for i in x:
    if 58>ord(i)>47:
        sum += int(i)
    else:
        y += i

y += str(sum)
print(y)
'''
