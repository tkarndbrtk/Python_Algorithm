i, j = map(int, input().split())

if i>j:
    tmp = j
    j = i
    i = tmp

k = 0
reList = [i,j]

while k <= 10: 
    k = i + j
    i = j
    j = k

    reList.append(k)

print(reList)
print(sum(reList))