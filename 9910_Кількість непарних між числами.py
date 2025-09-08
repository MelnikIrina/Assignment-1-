a, b = map(int, input().split())

min = min(a, b) + 1
max = max(a, b) - 1

if min > max:
    print(0)
else:
    c = (max + 1) // 2 - (min // 2)
    print(c)