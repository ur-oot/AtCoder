A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = [list(map(int, input().split())) for _ in range(M)]

c = min(a) + min(b)
for l in x:
    c = min(c, a[l[0] - 1] + b[l[1] - 1] - l[2])

print(c)
