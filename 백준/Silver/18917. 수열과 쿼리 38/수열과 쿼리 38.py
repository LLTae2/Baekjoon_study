# 1 x: A의 가장 뒤에 x를 추가한다.
# 2 x: A에서 x를 제거한다. A에 x가 두 개 이상 있는 경우에는 가장 앞에 있는 하나만 제거한다. 항상 A에 x가 있는 쿼리만 주어진다.
# 3: A에 포함된 모든 원소를 더한 값을 출력한다.
# 4: A에 포함된 모든 원소를 XOR한 값을 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
sumi = 0
xori = 0
for _ in range(n):
	sr = str(input()).split()
	a = sr[0]
	if a == '1':
		sumi += int(sr[1])
		xori ^= int(sr[1])
	elif a == '2':
		sumi -= int(sr[1])
		xori ^= int(sr[1])
	elif a == '3':
		print(sumi)
	else :
		print(xori)