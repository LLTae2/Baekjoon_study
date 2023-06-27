import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(1001)]
dis = [987654321 for _ in range(1001)]

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

def dijkstra(start):
	pq = []
	heapq.heappush(pq, (0, start))
	while pq:
		curE, curV = heapq.heappop(pq)
		if dis[curV] < curE:
			continue
		
		for i in graph[curV]:
			nxt, e = i
			if curE + e < dis[nxt]:
				dis[nxt] = curE + e
				heapq.heappush(pq, (dis[nxt], nxt))

start, end = map(int, input().split())
dijkstra(start)
print(dis[end])