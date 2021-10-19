N = int(input())
D = list(map(int, input().split()))

D.sort()
print(D[int(len(D) / 2)] - D[int(len(D) / 2) - 1])
