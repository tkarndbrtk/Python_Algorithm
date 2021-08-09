left = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in coins:
    if left>=i:
        cnt += left//i
        left %= i
print(cnt)