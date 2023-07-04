import heapq
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dijkstra(Map, dis):
	pq = []
	heapq.heappush(pq, (0, 0, Map[0][0]))
	dis[0][0] = Map[0][0]
	while pq:
		x, y, weight = heapq.heappop(pq)
		if weight < dis[x][y]:
			continue
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or nx >= n or ny < 0 or ny >= n:
				continue
			if dis[nx][ny] > weight + Map[nx][ny] or dis[nx][ny] == -1:
				dis[nx][ny] = weight + Map[nx][ny]
				heapq.heappush(pq, (nx, ny, weight + Map[nx][ny]))
a = 0
while True:
	a += 1
	n = int(input())
	if n == 0:
		break
	Map = []
	dis = [[-1 for _ in range(n)] for _ in range(n)]
	for _ in range(n):
		Map.append(list(map(int, input().split())))
	dijkstra(Map, dis)
	print(f'Problem {a}: {dis[-1][-1]}')