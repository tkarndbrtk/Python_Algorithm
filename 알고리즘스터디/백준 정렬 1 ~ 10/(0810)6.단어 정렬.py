import sys
num = int(sys.stdin.readline())
lst =[]
for i in range(num):
    word = sys.stdin.readline()
    lst.append(word)
my_set = set(lst)
my_lst = list(my_set)
my_lst.sort()
my_lst.sort(key=len)
for i in my_lst:
    print(i, end ='')