
N, r, c = map(int, input().split())
order = -1
row, col = r, c
num = N
for num in range(N, 1, -1):
    if row >= 2 ** (num - 1):
        order += 2 ** (2 * num - 1)
        row -= 2 ** (num - 1)
    if col >= 2 ** (num - 1):
        order += 2 ** (2 * (num - 1))
        col -= 2 ** (num - 1)

order += row * 2 + col + 1
print(order)



