N = int(input())

count = 0
ans = 1
for n in range(1, N + 1):
    tmpcount = 0
    tmpn = n
    while tmpn % 2 == 0 and tmpn != 1:
        tmpn /= 2
        tmpcount += 1
    if count < tmpcount:
        count = tmpcount
        ans = n

print(ans)
