import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(100001)]
dis = [987654321000 for _ in range(100001)]

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
	graph[b].append((a, c))
	
x, z = map(int, input().split())
p = int(input())
midNodes = list(map(int, input().split()))

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

ans = []

dijkstra(x)

for i in midNodes:
	ans.append(dis[i])
dis = [987654321000 for _ in range(100001)]

dijkstra(z)

for i in range(len(midNodes)):
	ans[i] += dis[midNodes[i]]

if min(ans) >= 987654321000:
	print(-1)
else:
	print(min(ans))