import sys
lst = []
num = int(sys.stdin.readline())
for n in range(num):
    lst.append(list(map(int,sys.stdin.readline().split())))
lst.sort(key=lambda x: (x[1], x[0]))
for i in lst:
    print(" ".join(map(str, i)))