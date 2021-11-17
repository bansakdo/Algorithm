
def DFS(X, cnt):
    global rst
    if cnt >= rst or X < 1:
        return
    elif X == 1:
        rst = min(rst, cnt)
    cnt += 1

    if X % 3 == 0:
        DFS(X // 3, cnt)
    if X % 2 == 0:
        DFS(X // 2, cnt)
    DFS(X - 1, cnt)


if __name__ == "__main__":
    X = int(input())
    rst = X
    DFS(X, 0)
    print(rst)


