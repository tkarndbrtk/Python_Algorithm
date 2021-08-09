'''
a = input()
print(a.count(" ")+1)
'''
#----------------------
'''
a = set(range(0,10001))
for i in range(10001):
    a.add(i+sum(map(int,str(i))))
    a.remove(i+sum(map(int,str(i))))
for c in a:
    print(c)
'''
#------------------------
'''
num= int(input())
sum_list=[]
for i in range(num):
    x = int(input())
    if x==0:
        sum_list.pop()
    else:
        sum_list.append(x)

print(sum(sum_list))
'''
#---------------------------
'''
t= ('a','b','c')
t = list(t)
t[0] = 'A'
t= tuple(t)
print(t)
'''
#--------------------
'''
a=dict(zip(['메로나','비비빅','죠스바'],[[300,20],[400,3],[250,100]]))
print(a)
'''
#------------------------------
'''
team = int(input())
for i in range(team):
    part = list(map(int,input().split()))
    num = part[0]
    del part[0]
    student=0
    av = sum(part)/num
    for j in part:
        if j>=av:
            student += 1
    print(100*(student/num))
'''
#--------------------
'''lst= input()
x= []
for i in lst:
'''
#------------------