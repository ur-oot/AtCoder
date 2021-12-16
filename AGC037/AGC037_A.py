S = input()

pre = ""
k = 0
i = 0

while i < len(S):
    c = S[i]
    if pre == c:
        i += 1
        if i == len(S):
            break
        c += S[i]
    pre = c
    k += 1
    i += 1

print(k)
