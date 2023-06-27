import heapq
import sys
input = sys.stdin.readline

n, m, k, start = map(int, input().split())

graph = [[] for _ in range(300001)]
dis = [987654321 for _ in range(300001)]

for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append((b, 1))

def dijkstra(start):
	pq = []
	heapq.heappush(pq, (0, start))
	dis[start] = 0
	while pq:
		curE, curV = heapq.heappop(pq)
		if dis[curV] < curE:
			continue
		
		for i in graph[curV]:
			nxt, e = i
			if curE + e < dis[nxt]:
				dis[nxt] = curE + e
				heapq.heappush(pq, (dis[nxt], nxt))

dijkstra(start)

ans = []
flag = 0
for i in range(len(dis)):
	if dis[i] == k:
		flag = 1
		print(i)
if flag == 0:
	print(-1)
	