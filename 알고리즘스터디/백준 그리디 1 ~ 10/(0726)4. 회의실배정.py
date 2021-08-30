import sys
council = int(sys.stdin.readline())
cnt = 1
lst = []
for i in range(council):
    lst.append(list(map(int,sys.stdin.readline().split())))
lst.sort(key = lambda x:(x[1], x[0]))
min_end = lst[0][1]
for i in range(1, len(lst)):
    if lst[i][0]>= min_end:
        cnt+=1
        min_end = lst[i][1]
print(cnt)
