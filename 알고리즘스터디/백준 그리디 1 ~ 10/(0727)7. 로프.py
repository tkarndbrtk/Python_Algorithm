'''
5
10
40
100
'''
n = int(input())
rope = []
max_kg = 0
for i in range(n):
    rope.append(int(input()))
rope.sort()
for i in range(len(rope)):
    if rope[i]*(len(rope)-i)  > max_kg:
        max_kg = rope[i]*(len(rope)-i)
print(max_kg)