A, B = map(int, input().split())
S = input()

ans = "Yes"
i = 0

for str in S:
    if i == A:
        if str != "-":
            ans = "No"
            break
    else:
        if str.isdecimal() == False:
            ans = "No"
            break
    i += 1

if i != A + B + 1:
    ans = "No"

print(ans)
