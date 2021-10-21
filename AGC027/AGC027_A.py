N, x = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

num = 0
for i, an in enumerate(A):
    if i != len(A) - 1:
        if x >= an:
            x -= an
            num += 1
    else:
        if x == an:
            num += 1

print(num)
