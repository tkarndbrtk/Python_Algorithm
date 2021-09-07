import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  q = []

  heapq.heappush(q, (0, start))
  distance[start] = 0 # @ 시작지점에서 시작지점까지의 최단거리는 0!
  while q:
    # @ 간선정보(line_information) 중에 이전 노드에서 가장 최단 거리의 현재 노드(now), 거리(dist) 설정 
    dist, now = heapq.heappop(q) 
    # @ 필요없는 반복문을 제거 --> 시작노드에서 현재 노드까지의 최단거리가 간선정보에서 받은 큐의 최단거리보다 클 경우는 생략
    if distance[now] < dist:
      continue
    # @ 현재 노드까지의 최단거리 + 현재노드 -> 다른 노드로 가는 거리(큐에 있는 간선 정보) = 시작노드에서 다른 노드까지의 거리(cost)
    for i in line_information[now]:
      cost = dist + i[1]
    # @ 기존 distance 리스트에 저장되어 있는 시작노드에서의 다른 노드까지의 거리 vs 방금 큐의 정보와 다른 노드까지의 거리를 합산한 거리(cost)
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

node_num, line_num = map(int,input().split())
start_node = int(input())
line_information = [[] for i in range(node_num+1)]
distance = [INF] * (node_num+1)

for _ in range(line_num):
  from_node, to_node, cost = map(int, input().split())
  line_information[from_node].append((to_node, cost))

dijkstra(start_node)

for i in range(len(distance)-1):
  if distance[i+1] == INF:
    print('INF')
  else:
    print(distance[i+1])