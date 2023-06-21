import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

parent = [i for i in range(500001)]

num = 0

def find(x):
	if x == parent[x]:
		return x
	parent[x] = find(parent[x])
	return parent[x]

def union(x, y):
	x = find(x)
	y = find(y)
	parent[x] = y

n, m = map(int, input().split())
for i in range(1, m+1):
	a, b = map(int, input().split())
	if find(a) != find(b):
		union(a, b)
	else :
		num = i
		break

print(num)