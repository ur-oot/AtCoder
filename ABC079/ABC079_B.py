N = int(input())

LN = []

for i in range(N + 1):
    if i == 0:
        LN.append(2)
    elif i == 1:
        LN.append(1)
    else:
        LN.append(LN[i - 2] + LN[i - 1])

print(LN[N])
