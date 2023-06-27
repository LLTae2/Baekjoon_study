import heapq
import sys
input = sys.stdin.readline

dis = [9876543210 for _ in range(20001)]

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(20001)]
for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

def dijkstra(start):
	pq = []
	heapq.heappush(pq, (0, start))
	dis[start] = 0
	while pq:
		e, v = heapq.heappop(pq)
		if dis[v] < e:
			continue
		for i in graph[v]:
			nxt = i[0]
			cost = i[1]
			if dis[v] + cost < dis[nxt]:
				dis[nxt] = dis[v] + cost
				heapq.heappush(pq, (dis[nxt], nxt))
dijkstra(start)
for i in range(1, n+1):
	if dis[i] == 9876543210:
		print("INF")
	else:
		print(dis[i])