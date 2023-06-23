import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

n, m = map(int, input().split())

visited = [[False] * m for _ in range(n)]

graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

def dfs(x, y):
	visited[x][y] = True
	graph[x][y] = 0
	for i in range(8):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if nx < 0 or nx >= n or ny < 0 or ny >= m:
			continue
		if visited[nx][ny]:
			continue
		if graph[nx][ny] == 0:
			continue
		
		dfs(nx, ny)

cnt = 0

for i in range(len(graph)):
	for j in range(len(graph[i])):
		if graph[i][j] == 1:
			cnt += 1
			dfs(i, j)

print(cnt)