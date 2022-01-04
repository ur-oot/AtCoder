X = int(input())

tmpMax = 1
if tmpMax == X:
    print(tmpMax)
    exit()

for b in range(2, 100):
    p = 2
    if b ** p > X:
        break
    while b ** p <= X:
        p += 1
    tmpMax = max(tmpMax, b ** (p - 1))

print(tmpMax)
