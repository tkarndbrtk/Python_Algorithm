import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  q = []

  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue

    for i in line_information[now]:
      time = dist + i[1]

      if time < distance[i[0]]:
        distance[i[0]] = time
        heapq.heappush(q, (time, i[0]))

node_num, line_num, start_node = map(int,input().split())
line_information = [[] for i in range(node_num+1)]
distance = [INF] * (node_num+1)

for _ in range(line_num):
  from_node, to_node, cost = map(int, input().split())
  line_information[from_node].append((to_node, cost))

dijkstra(start_node)

count = 0
max_distance = 0
for d in distance:
  if d != 1e9:
    count+=1
    max_distance = max(max_distance, d)
print(count-1, max_distance)