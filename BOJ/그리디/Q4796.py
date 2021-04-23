import sys



cnt = 0
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    cnt += 1

    result = (V // P) * L
    rest = V % P
    result += (L if rest > L else rest)
    print("Case %d: %d" %(cnt, result))
# sys.exit(0)
