s = int(input())

a = [s]

for i in range(1, 1000001):
    if a[i - 1] % 2 == 0:
        fn = a[i - 1] // 2
    else:
        fn = 3 * a[i - 1] + 1
    if fn in a:
        print(i + 1)
        break
    else:
        a.append(fn)
