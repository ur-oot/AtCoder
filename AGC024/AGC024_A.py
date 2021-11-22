A, B, C, K = map(int, input().split())

N = [A, B, C]

if abs(N[0] - N[1]) > 10**18:
    print("Unfair")
    exit()

if K % 2 == 0:
    print(N[0] - N[1])
else:
    print(N[1] - N[0])
