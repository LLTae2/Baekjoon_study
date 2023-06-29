import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(100001)]
dis = [9876543210 for _ in range(100001)]
for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
x, y, z = map(int, input().split())
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
def dijkstra2(start):
	pq = []
	heapq.heappush(pq, (0, start))
	while pq:
		curE, curV = heapq.heappop(pq)
		if dis[curV] < curE:
			continue
		
		for i in graph[curV]:
			nxt, e = i
			if nxt == y:
				continue
			if curE + e < dis[nxt]:
				dis[nxt] = curE + e
				heapq.heappush(pq, (dis[nxt], nxt))
ans = []
dijkstra(x)
ans.append(dis[y])
dis = [9876543210 for _ in range(100001)]
dijkstra(y)
ans[0] += dis[z]
dis = [9876543210 for _ in range(100001)]
dijkstra2(x)
ans.append(dis[z])
for i in ans:
	if i >= 9876543210:
		print(-1, end=' ')
	else:
		print(i, end=' ')