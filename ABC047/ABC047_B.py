W, H, N = map(int, input().split())

array = [[1 for _ in range(W)] for _ in range(H)]

for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        for j in range(H):
            for i in range(x):
                array[j][i] = 0
    elif a == 2:
        for j in range(H):
            for i in range(x, W):
                array[j][i] = 0
    elif a == 3:
        for j in range(y):
            for i in range(W):
                array[j][i] = 0
    elif a == 4:
        for j in range(y, H):
            for i in range(W):
                array[j][i] = 0

print(sum(sum(row) for row in array))
