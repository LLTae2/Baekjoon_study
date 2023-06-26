from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ladders = []
snakes = []
arr = [0 for _ in range(101)]
visited = [False] * 101

for _ in range(n):
	a, b = map(int, input().split())
	arr[a] = b
for _ in range(m):
	a, b = map(int, input().split())
	arr[a] = b
	
def bfs():
	q = deque()
	q.append([1, 0])
	visited[1] = True
	while q:
		x, cnt = q.popleft()
		if x == 100:
			return cnt
	
		for i in range(1, 7):
			if x+i > 100:
				continue
			if arr[x+i] != 0:
				if not visited[arr[x+i]]:
					visited[arr[x+i]] = True
					q.append([arr[x+i], cnt+1])
			else :
				if not visited[x+i]:
					visited[x+i] = True
					q.append([x + i, cnt+1])

print(bfs())
