S = input()

ans = 0
tmp = 0

for str in S:
    if str in "ACGT":
        tmp += 1
        ans = max(ans, tmp)
    else:
        tmp = 0

print(ans)
