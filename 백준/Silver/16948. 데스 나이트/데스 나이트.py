from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

n = int(input())
curX, curY, tarX, tarY = map(int, input().split())

visited = [[0 for i in range(n+1)] for _ in range(n)]

answer = []

def bfs():
	q = deque()
	q.append([curX, curY, 0])
	visited[curX][curY] = 1
	while q:
		# for i in visited:
		# 	print(*i)
		# print()
		x, y, cnt = q.popleft()
		if x == tarX and y == tarY:
			return cnt
		for i in range(6):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if nx >= n or nx < 0 or ny >= n or ny < 0:
				continue
			if visited[nx][ny] == 1:
				continue
				
			visited[nx][ny] = 1
			q.append([nx, ny, cnt+1])
	return -1
print(bfs())
