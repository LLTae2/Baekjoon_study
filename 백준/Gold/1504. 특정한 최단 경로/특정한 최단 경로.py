import heapq
import sys
input = sys.stdin.readline

dis = [9876543210 for _ in range(801)]

n, m = map(int, input().split())

graph = [[] for _ in range(801)]
for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
	graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
	pq = []
	heapq.heappush(pq, (0, start))
	dis[start] = 0
	
	while pq:
		e, v = heapq.heappop(pq)
		if dis[v] < e:
			continue
		for nxt, cost in graph[v]:
			if dis[v] + cost < dis[nxt]:
				dis[nxt] = dis[v] + cost
				heapq.heappush(pq, (dis[nxt], nxt))

sumi = 0

dijkstra(1)
sumi += dis[v1]
dis = [9876543210 for _ in range(801)]
dijkstra(v1)
sumi += dis[v2]
dis = [9876543210 for _ in range(801)]
dijkstra(v2)
sumi += dis[n]

sumi2 = 0

dis = [9876543210 for _ in range(801)]
dijkstra(1)
sumi2 += dis[v2]
dis = [9876543210 for _ in range(801)]
dijkstra(v2)
sumi2 += dis[v1]
dis = [9876543210 for _ in range(801)]
dijkstra(v1)
sumi2 += dis[n]
if min(sumi, sumi2) >= 9876543210:
	print(-1)
else:
	print(min(sumi, sumi2))