n = int(input())
arr = []
sumi = 0
for _ in range(n):
	m = int(input())
	if m == 0:
		a = arr.pop()
		sumi -= a
	else:
		arr.append(m)
		sumi += m
print(sumi)