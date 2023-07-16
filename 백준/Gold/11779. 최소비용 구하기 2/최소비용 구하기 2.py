import sys
input = sys.stdin.readline
import heapq

graph = [[] for _ in range(1001)]
dis = [9876543210 for _ in range(1001)]
bt = [0 for _ in range(1001)]

n = int(input())
m = int(input())

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

start, end = map(int, input().split())

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
				bt[nxt] = curV
				dis[nxt] = curDis + e
				heapq.heappush(pq, (dis[nxt], nxt))

ans = [end]
dijkstra(start)
print(dis[end])
prev = end
while True:
	if prev == start:
		break
	ans.append(bt[prev])
	prev = bt[prev]
print(len(ans))
print(*reversed(ans))