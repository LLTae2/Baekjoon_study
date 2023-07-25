import sys
input = sys.stdin.readline
import heapq

n, m, x = map(int, input().split())

graph = [[] for _ in range(1001)]
answer = [-1 for _ in range(1001)]
dis = [98765432100 for _ in range(1001)]

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

def dijkstra(start):
	pq = []
	heapq.heappush(pq, (0, start))
	dis[start] = 0

	while pq:
		curDis, curV = heapq.heappop(pq)
		if dis[curV] < curDis:
			continue
		for nxt, e in graph[curV]:
			if dis[nxt] > curDis + e:
				dis[nxt] = curDis + e
				heapq.heappush(pq, (dis[nxt], nxt))

dijkstra(x)
for i in range(1, n+1):
	answer[i] = dis[i]
for i in range(1, n+1):
	dis = [98765432100 for _ in range(1001)]
	dijkstra(i)
	answer[i] += dis[x]

print(max(answer))
