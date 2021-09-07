# #? 서로소 집합 자료구조
def find_parent(parent, x):
  if parent[x] !=x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
'''
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
  parent[i] = i

for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

print('각 원소가 속한 집합:', end='')
for i in range(1, v+1):
  print(find_parent(parent, i), end=' ')

print()

print('부모테이블:', end='')
for i in range(1, v+1):
  print(parent[i], end=' ')
'''
#---------------------------------------
#? 서로소 집합을 이용한 사이클판별
'''
v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
  parent[i] = i

cycle = False

for i in range(e):
  a, b = map(int, input().split())

  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  else:
    union_parent(parent, a, b)

if cycle:
  print("사이클 발생")
else:
  print("사이클 미발생")
'''
#---------------------------------------
#? 위 두가지를 이용한 크루스칼 알고리즘

v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
  parent[i] = i

for _ in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
  
print(result)