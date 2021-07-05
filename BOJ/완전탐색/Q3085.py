


tot = 0
__list = list(map(int, input().split()) for _ in range(11))
for D, V in __list:
    tot += D + (20 * V)

print(tot)



