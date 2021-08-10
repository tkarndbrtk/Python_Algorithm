import sys
lst =[]
a = int(sys.stdin.readline())
for i in range(a):
    lst.append(list(sys.stdin.readline().split()))
lst.sort(key = lambda x : int(x[0]))
for i in lst:
    print(" ".join(i))
