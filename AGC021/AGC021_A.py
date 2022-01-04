N = int(input())

ansN = str(N)[0] + "9" * (len(str(N)) - 1)
ans = sum(map(int, ansN))

if int(ansN) > N:
    ans -= 1

print(ans)
