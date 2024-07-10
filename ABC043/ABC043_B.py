s = list(input())

result = []

for char in s:
    if char == "B":
        if len(result) > 0:
            result.pop()
    else:
        result.append(char)

print("".join(result))
