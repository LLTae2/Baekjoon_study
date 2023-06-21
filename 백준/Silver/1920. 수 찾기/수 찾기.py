

n = int(input())
data = sorted(list(map(int, input().split())))

m = int(input())
arr = list(map(int, input().split()))

def binarySearch(start, end, target):
	if start > end:
		return False
	mid = (start + end) // 2
	
	if data[mid] == target:
		return True
	
	elif data[mid] > target:
		return binarySearch(start, mid-1, target)
	
	else :
		return binarySearch(mid+1, end, target)

for i in arr:
	if binarySearch(0, n-1, i):
		print(1)
	else :
		print(0)