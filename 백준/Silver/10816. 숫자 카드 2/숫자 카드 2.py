n = int(input())
data = sorted(list(map(int, input().split())))

m = int(input())
arr = list(map(int, input().split()))


def binarySearchStart(start, end, target):
	while start <= end:
		mid = (start + end) // 2
		if data[mid] == target:
			if mid-1 < 0 or data[mid-1] != target:
				return mid
			else :
				end = mid-1
		elif data[mid] >= target:
			end = mid-1
		else :
			start = mid+1
	return -1

def binarySearchEnd(start, end, target):
	while start <= end:
		mid = (start + end) // 2
		if data[mid] == target:
			if mid == end or data[mid+1] != target:
				return mid
			else :
				start = mid+1
		elif data[mid] >= target:
			end = mid-1
		else :
			start = mid+1
	return -1

answer = []

for i in arr:
	if binarySearchEnd(0, n-1, i) == binarySearchStart(0, n-1, i) == -1:
		answer.append(0)
	else :
		answer.append(binarySearchEnd(0, n-1, i) - binarySearchStart(0, n-1, i) + 1)
print(*answer)
