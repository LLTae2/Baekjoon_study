times = int(input())

dic = dict()
cnt = 0

parent = [i for i in range(200001)]
size = [1 for i in range(200001)]

def find(x):
	if x == parent[x]:
		return x
	parent[x] = find(parent[x])
	return parent[x]

def union(x, y):
	x = find(x)
	y = find(y)
	if x != y:
		parent[x] = y
		size[y] += size[x]

for i in range(times):
	cases = int(input())
	parent = [j for j in range(200001)]
	size = [1 for j in range(200001)]
	cnt = 0
	dic = {}
	for j in range(cases):
		a, b = map(str, input().split())
		
		if a not in dic:
			dic[a] = cnt
			cnt += 1
		if b not in dic:
			dic[b] = cnt
			cnt += 1
		
		union(dic[a], dic[b])
		print(size[find(dic[a])])
		