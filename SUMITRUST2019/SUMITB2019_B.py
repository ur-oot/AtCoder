N = int(input())

for X in range(1, N + 1):
    if int(X * 1.08) == N:
        print(X)
        exit()

print(":(")
