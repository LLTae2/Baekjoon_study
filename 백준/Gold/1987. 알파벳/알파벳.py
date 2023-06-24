import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
Map = []
visited = [0 for _ in range(26)]
for _ in range(n):
	Map.append(list(input()))
Max = 0
def dfs(x, y, cnt):
	global Max
	if cnt > Max:
		Max = cnt
		
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if nx < 0 or nx == n or ny < 0 or ny == m:
			continue
		if visited[ord(Map[nx][ny]) - 65] == 1:
			continue
		visited[ord(Map[nx][ny]) - 65] = 1
		dfs(nx, ny, cnt+1)
		visited[ord(Map[nx][ny]) - 65] = 0
visited[ord(Map[0][0]) - 65] = 1
dfs(0, 0, 1)
print(Max)