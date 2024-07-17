s = input()
n = len(s)
result = 0

for i in range(1 << (n - 1)):
    tmp = [int(s[0])]
    for j in range(n - 1):
        if (i >> j) & 1:
            tmp.append(int(s[j + 1]))
        else:
            tmp[-1] = int(str(tmp[-1]) + s[j + 1])
    result += sum(tmp)

print(result)
