#1번
'''
num = int(input())
group = []
for i in range(num):
    kg, cm = map(int,input().split())
    group.append([kg, cm, 1])

for j in range(num):
    for k in range(num):
        if group[j][0] < group[k][0] and group[j][1] < group[k][1]:
            group[j][2] +=1
        else:
            continue

for l in range(5):
    print(group[l][2], end = ' ')
'''
# 2번
'''
while 'a':
    num1 , num2 = map(int,input().split())
    print(num1+num2)
'''
# 3번, 4번 내문제

# 5번
'''
num = int(input())
x = []
sum = 0
x = list(map(int,input().split()))
if len(x) != num:
    print("개수 오류")
x.sort()
for i in range(num):
    sum += x[i] * (len(x) -i)
print(sum)
'''
# 6번
num = int(input())
for i in range(num):
    for j in range(num-i-1):
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    print('')