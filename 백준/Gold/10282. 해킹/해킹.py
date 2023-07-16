import sys
input = sys.stdin.readline

import heapq

graph = [[] for _ in range(10001)]
dis = [987654321 for _ in range(10001)]
ans = []

def dijkstra(start):
	pq = []
	heapq.heappush(pq, (0, start))
	dis[start] = 0
	ans.append(start)
	
	while pq:
		curDis, curV = heapq.heappop(pq)
		if dis[curV] < curDis:
			continue
		for nxt, e in graph[curV]:
			if dis[nxt] > curDis + e:
				dis[nxt] = curDis + e
				ans.append(nxt)
				heapq.heappush(pq, (dis[nxt], nxt))

n = int(input())

for _ in range(n):
	graph = [[] for _ in range(10001)]
	dis = [987654321 for _ in range(10001)]
	ans = []
	v, d, c = map(int, input().split())
	for _ in range(d):
		a, b, s = map(int, input().split())
		graph[b].append((a, s))
	dijkstra(c)
	maxi = 0
	for i in ans:
		if dis[i] > maxi:
			maxi = dis[i]
	print(len(set(ans)), maxi)
	