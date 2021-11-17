

n = int(input())
size = len(str(n))

if n > 9 * size:
    t = n - (9 * size)
else:
    t = n // 2

while t < n:
    individual = 0
    for x in str(t):
        individual += int(x)
    if t + individual == n:
        break
    t += 1

if t == n:
    print(0)
else:
    print(t)
