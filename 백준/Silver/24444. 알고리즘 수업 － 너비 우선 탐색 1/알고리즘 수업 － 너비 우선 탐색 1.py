from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

v, e, start = map(int, input().split())

graph = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
answer = [0 for _ in range(v+1)]

for _ in range(e):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)


def bfs(start):
	cnt = 1
	q = deque([start])
	visited[start] = True
	answer[start] = 1
	while q:
		a = q.popleft()
		for i in sorted(graph[a]):
			if not visited[i]:
				cnt += 1
				visited[i] = True
				q.append(i)
				answer[i] = cnt

bfs(start)
for i in range(1, v+1):
	print(answer[i])