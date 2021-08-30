import sys
n = int(sys.stdin.readline())
#dp 테이블
d = [0] * (n+1)

d[0]=1
d[1]=2

for i in range(3, n+1):
	d[i] = ((d[i-1] + d[i-2])%10007)

print(d[n])