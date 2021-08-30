import sys

times = int(sys.stdin.readline())
num =[]
cnt = [0] * 10001
for i in range(times):
    a = (int(sys.stdin.readline()))
    cnt[a] += 1
    
for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i)