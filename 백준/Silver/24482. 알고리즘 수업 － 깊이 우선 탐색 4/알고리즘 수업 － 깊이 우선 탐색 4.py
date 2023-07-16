import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e, start = map(int, input().split())

graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)

for _ in range(e):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

answer = [-1 for _ in range(v+1)]

def dfs(v, cnt):
	answer[v] = cnt
	visited[v] = True
	for i in reversed(sorted(graph[v])):
		if not visited[i]:
			dfs(i, cnt+1)

dfs(start, 0)
for i in range(1, v+1):
	print(answer[i])