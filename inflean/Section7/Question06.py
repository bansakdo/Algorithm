import sys


sys.stdin = open("input.txt", "rt")


# 6번 문제. 알파코드(DFS)

# 내 풀이
'''
def DFS(L):
    global cnt, res
    if L == length:
        for x in res:
            print(x, end='')
        print()
        cnt += 1
    elif L < length:
        if a[L] == '0':
            # sys.exit(0)
            return
        res.append(chr(int(a[L]) + 64))
        # print("1:", int(a[L]))
        # print(res)
        DFS(L + 1)
        res.pop()
        if L + 1 < length and int(a[L:L+2]) <= 26:
            res.append(chr(int(a[L:L+2]) + 64))
            # print("2:", int(a[L:L+2]))
            # print(res)
            DFS(L + 2)
            res.pop()


if __name__ == "__main__":
    a = str(input())
    res = []
    length = len(a)
    cnt = 0

    DFS(0)
    print(cnt)
'''


# 해설

def DFS(L, P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P):
            print(chr(res[j] + 64), end=' ')
        print()
    else:
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i
                DFS(L + 1, P + 1)
            elif i > 10 and code[L] == i // 10 and code[L + 1] == i % 10:
                res[P] = i
                DFS(L + 2, P + 1)


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)
    res = [0] * (n + 3)
    cnt = 0
    DFS(0, 0)
    print(cnt)


