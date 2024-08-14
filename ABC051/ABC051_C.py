sx, sy, tx, ty = map(int, input().split())

dx = tx - sx
dy = ty - sy

# Path 1
print("U" * dy + "R" * dx, end="")

# Path 2
print("D" * dy + "L" * dx, end="")

# Path 3
print("L" + "U" * (dy + 1) + "R" * (dx + 1) + "D", end="")

# Path 4
print("R" + "D" * (dy + 1) + "L" * (dx + 1) + "U")
