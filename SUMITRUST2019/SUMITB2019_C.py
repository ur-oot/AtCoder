X = int(input())

d, m = divmod(X, 100)
ans = 0

if m <= 5 * d:
    ans = 1

print(ans)
