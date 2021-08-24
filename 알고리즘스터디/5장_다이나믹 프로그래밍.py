# #! 비효율적인 코드
'''
def fibo(x):
	if x == 1 or x == 2:
		return 1
	return fibo(x-1) + fibo(x-2)
'''
#@ 다이나믹 이용한 탑다운

'''
d =[0]*100
def fibo(x):

  if x==0 or x==1:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]
'''

#@ 다이나믹 이용한 바텀업
'''
d = [0]*100
d[1] = 1
d[2] = 1
n = 99
for i in range(3, n+1):
  d[i] = d[i-1] +d[i-2]
print(d[n])
'''

#? 개미의 식량털기
'''
import sys
num = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
sum = 0
d = [0] * 100
d[0] = lst[0]
d[1] = max(lst[0], lst[1])
for i in range(2,num):
  d[i] = max(d[i-1],d[i-2]+lst[i])

print(d[num-1])
'''
#? 1로 만들기
import sys
num = int(sys.stdin.readline())
time = 0
def make_one(num, time):
  while 1:
    if num == 1:
      break
    time += 1
    if num % 5 == 0:
      num = num / 5
      continue
    elif num % 3 == 0:
      num = num / 3
      continue
    elif num % 2 == 0:
      num = num / 2
      continue
    else:
      num-=1
  return time
print(make_one(num, time))

