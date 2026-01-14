n, x = map(int, input().split())
nums = list(map(int, input().split()))

re = []

for i in nums:
    if i < x:
        re.append(i)
print(*re)
