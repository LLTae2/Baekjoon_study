from collections import deque

n, k = map(int, input().split())
q = deque()
q.append([n, 0])
cases = []
visited = [-2 for _ in range(200001)]
# visited[]
while q:
	x, cnt = q.popleft()
	if x == k:
		print(cnt)
		break
	# print(x)
	if x-1 < 0 and x != 0:
		continue
	if x < 100001:
		if visited[x-1] == -2:
			visited[x-1] = x
			q.append([x-1, cnt+1])
		if visited[x+1] == -2:
			visited[x+1] = x
			q.append([x+1, cnt+1])
		if visited[x*2] == -2:
			visited[x*2] = x
			q.append([x*2, cnt+1])
	
ans = [k]
while ans[-1] != n:
	bef = ans[-1]
	ans.append(visited[bef])
	
print(*reversed(ans))


