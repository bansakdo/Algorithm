import sys

sys.stdin = open("input.txt", "rt")

# 3번 문제. 도전과제. 계단오르기(Top-down, 메모이제이션)


# 내 풀이
'''
def DFS(l, a, b):
    global cnt
    if l == 0:
        # cnt += 1
        return 1
    elif l < 0:
        return 0
    else:
        if l in mem.keys():
            v = mem[l]
        else:
            v1 = DFS(l - 1, a + 1, b)
            v2 = DFS(l - 2, a, b + 1)
            v = v1 + v2
            mem[l] = v
        return v



if __name__ == "__main__":
    n = int(input())
    cnt = 0
    mem = dict()

    print(DFS(n, 0, 0))
'''

# 풀이 2

def DFS(len):
    if dy[len] > 0:
        return dy[len]
    if len == 2 or len == 1:
        return len
    else:
        dy[len] = DFS(len - 1) + DFS(len - 2)
        return dy[len]



if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n + 1)

    print(DFS(n))


