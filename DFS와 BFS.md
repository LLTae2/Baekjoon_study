


```python
from collections import deque

def dfs(v):
	if visited[v]:
		return
	visited[v] = True
	print(v, end=' ')
	for i in graph[v]:
			dfs(i)

def bfs(v):
	visited = [False] * (n+1)
	visited[v] = True
	q = deque()
	q.append(v)
	while q:
		x = q.popleft()
		print(x, end=' ')
		for i in graph[x]:
			if not visited[i]:
				q.append(i)
				visited[i] = True

n, l, s = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(l):
	a, b = map(int, input().split())
	graph[b].append(a)
	graph[a].append(b)
for i in range(n+1):
	graph[i].sort()
visited = [False] * (n+1)

dfs(s)
print()
bfs(s)
```
	
