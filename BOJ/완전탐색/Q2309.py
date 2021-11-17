
'''
20
7
23
19
10
15
25
8
13

'''


# '''

import sys
def DFS(L, l):
    global res

    if L == 7:
        s = sum(res)
        if s == 100:
            res.sort()
            for x in res:
                print(x)
            sys.exit()

    else:
        for i in range(l, 9):
            res[L] = height[i]
            DFS(L+1, i+1)


if __name__ == "__main__":
    height = []
    for _ in range(9):
        height.append(int(input()))
    res = [0] * 7

    DFS(0, 0)
# '''






