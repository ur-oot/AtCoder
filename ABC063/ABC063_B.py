S = input()

ans = "yes"

for s in S:
    if S.count(s) > 1:
        ans = "no"
        break

print(ans)
