sum = 0
arr = list(map(int, input().split()))
for i in arr:
    sum += i**2
print(sum%10)