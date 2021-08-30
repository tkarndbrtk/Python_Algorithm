num, money = map(int,input().split())
count = 0
unit_group =[]
for i in range(num):
    unit = int(input())
    unit_group.append(unit)
unit_group.reverse()

for coin in unit_group:
    if money >= coin:
        count += money//coin
        money %= coin
    elif money==0:
        break
print(count)