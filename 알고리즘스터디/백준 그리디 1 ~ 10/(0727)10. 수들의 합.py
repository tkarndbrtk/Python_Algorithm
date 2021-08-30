s = int(input())
n = 0
while 1:
    if s > n:
        n+=1 
        s-=n
    else:
        break
print(n)