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

ccnt = 0

def dfs(v, cnt):
	global ccnt
	ccnt += 1
	answer[v] = cnt * ccnt
	visited[v] = True
	for i in sorted(graph[v]):
		if not visited[i]:
			dfs(i, cnt+1)

dfs(start, 0)
for i in range(len(answer)):
	if answer[i] == -1:
		answer[i] = 0
print(sum(answer[1:v+1]))