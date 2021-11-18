
n, k = map(int, input().split())

order = -1
circle = [n for n in range(1, n + 1)]
rst = []
while circle:
    order += k
    order %= len(circle)
    rst.append(circle.pop(order))
    order -= 1

print("<", end='')
print(*rst, sep=', ', end='')
print(">")


'''
1 2 3 4 5 6 7
1 2 4 5 6 7
1 2 4 5 7
1 4 5 7
1 4 5
1 4
'''