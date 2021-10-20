N, M, X = map(int, input().split())
A = list(map(int, input().split()))

left = right = 0

for am in A:
    if am < X:
        left += 1
    else:
        right += 1

print(min(left, right))
