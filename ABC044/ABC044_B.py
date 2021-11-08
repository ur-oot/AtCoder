w = input()

ans = 'Yes'
for c in w:
    if w.count(c) % 2 != 0:
        ans = "No"
        break

print(ans)
