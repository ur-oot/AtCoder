N = int(input())
A = list(map(int, input().split()))

MOD = 10**9 + 7

counts = {}
for num in A:
    if num != 0:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

result = 1
for num, count in counts.items():
    if count == 1:
        result = 0
        break
    result = (result * count) % MOD

print(result)
