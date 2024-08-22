mod = 10**9 + 7


def prime_factorization(n):
    factors = {}
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    if n > 1:
        factors[n] = 1
    return factors


N = int(input())

# N!の素因数分解を取得
factors = {}
for i in range(2, N + 1):
    for prime, count in prime_factorization(i).items():
        factors[prime] = factors.get(prime, 0) + count

# 約数の個数を計算
divisor_count = 1
for count in factors.values():
    divisor_count *= count + 1

# 階乗の約数の個数を表示
print(divisor_count % mod)
