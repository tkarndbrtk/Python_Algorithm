#1번
'''
string = "  123   456   ABC    "
a =''
str_list = []
string= string.strip()
string +=" "
print(string)
for i in range(len(string)):
    if string[i] !=' ':
        a += string[i]
    elif string[i-1] !=' ' and string[i] ==' ':
        str_list.append(a)
        a = ''
print(str_list)
'''
#2번
'''
a = int(input())
for i in range(1,a+1,1):
    print(i)
'''
#3번
'''
a = list(map(int, input().split()))
a.sort()
for i in range(10):
    if a[i+1]<=10:
        a.append(int(a[i] + a[i+1]))
    else:
        a.pop()
        break
print(a)
print(sum(a))
'''
string = "  123   456   ABC    "
r_list =[ ]

import re  #정규표현식 모듈 불러오기

rr = re.sub(' +','',string) #' +'의 의미 : 공백이 1개 이상발생 함을 의미
r_list=[rr[0:3],rr[3:6],rr[6:9]]
print(r_list)