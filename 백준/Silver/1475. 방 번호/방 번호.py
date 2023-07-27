import math
N = input()

arr = [0 for _ in range(10)]

for i in N:
	arr[int(i)] += 1
arr[6] = arr[9] = math.ceil((arr[6] + arr[9]) / 2)
for i in range(len(arr)):
	if arr[i] == max(arr):
		print(arr[i])
		break