
N, B = map(int, input().split())

changed = ''
while N > 0:
    N, tmp = divmod(N, B)
    if tmp >= 10:
        tmp = chr(tmp + 55)
    changed += str(tmp)

print(changed[::-1])