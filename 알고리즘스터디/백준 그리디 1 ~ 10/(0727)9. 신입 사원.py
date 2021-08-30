'''
1 4
2 3
3 2
4 1
5 5
'''

cases = int(input())
cnt = 0
for i in range(cases):
    person = int(input())
    cnt = person
    lst = []
    for i in range(person):
        lst.append(list(map(int,input().split())))
    for i in range(person):
        for j in range(person):
            if lst[i][0] > lst[j][0] and lst[i][1] > lst[j][1]:
                cnt -=1
                break
    print(cnt)