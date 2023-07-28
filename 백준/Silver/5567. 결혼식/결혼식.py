import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(501)]
visited = [False] * 501

for _ in range(m):
	a, b = map(int, input().split())
	graph[b].append(a)
	graph[a].append(b)
	
cnt = 0

def bfs(v):
	global cnt
	q = deque()
	q.append([v, 0])
	while q:
		v, depth = q.popleft()
		if depth >= 2:
			continue
		for i in graph[v]:
			if not visited[i]:
				visited[i] = True
				q.append([i, depth+1])
				cnt += 1

visited[1] = True
bfs(1)
print(cnt)