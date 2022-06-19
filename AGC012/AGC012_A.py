N = int(input())
AN = list(map(int, input().split()))

sortAN = sorted(AN)

print(sum(sortAN[N:][::2]))
