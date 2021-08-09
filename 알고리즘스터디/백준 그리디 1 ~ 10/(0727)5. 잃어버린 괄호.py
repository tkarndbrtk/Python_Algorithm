x = input()
minus_lst=[]
x = x.replace('+',' ')
x = x.replace('-',' ')
x = x.split()
sum = float(x[0])
for i in range(1,len(x)):
    sum-=float(x[i])

print(sum)
