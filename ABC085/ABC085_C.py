N, Y = map(int, input().split())

x = y = z = -1

for i in range(0, N + 1):
    for j in range(0, N + 1 - i):
        if 10000 * i + 5000 * j + 1000 * (N - i - j) == Y:
            x = i
            y = j
            z = N - i - j
            break
    else:
        continue
    break

print(x, y, z)
