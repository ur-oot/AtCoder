S = input()

compressed = ""
prev_char = None

for char in S:
    if char != prev_char:
        compressed += char
        prev_char = char

ans = 2 * min(compressed.count('B'), compressed.count('W'))

if compressed[0] != compressed[-1]:
    ans -= 1

print(ans)
