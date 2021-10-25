import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

j = list(itertools.permutations(range(1, N + 1)))

print(abs(j.index(P) - j.index(Q)))
