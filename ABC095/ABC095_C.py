A, B, C, X, Y = map(int, input().split())

tyoku = A * X + B * Y
mix = min(X, Y) * 2 * C
bun = max(X, Y) * 2 * C
if X > Y:
    mix += (X - Y) * A
elif X < Y:
    mix += (Y - X) * B

print(min(tyoku, mix, bun))
