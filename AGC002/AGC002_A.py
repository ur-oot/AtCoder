a, b = map(int, input().split())

if a <= 0 <= b:
    print("Zero")
else:
    if a > 0:
        print("Positive")
    else:
        if (a - b - 1) % 2 == 0:
            print("Positive")
        else:
            print("Negative")
