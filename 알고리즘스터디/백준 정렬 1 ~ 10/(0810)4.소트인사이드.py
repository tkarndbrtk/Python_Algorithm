import sys
num = int(sys.stdin.readline())
lst = list(map(int,list(str(num))))
lst.sort(reverse=True)
print("".join(map(str, lst)))