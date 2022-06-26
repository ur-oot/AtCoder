N = int(input())
HN = list(map(int, input().split()))

if N == 1:
    print("Yes")
    exit()

for i in range(N - 1, 0, -1):
    df = HN[i - 1] - HN[i]
    if df >= 2:
        print("No")
        exit()
    elif df == 1:
        HN[i - 1] -= 1

print("Yes")
