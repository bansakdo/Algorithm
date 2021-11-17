'''

9 3
1 2 3 4 5 6 7 8 9
=> 17


9 4
2 2 2 3 4 5 6 7 9
=> 13

9 4
2 2 7 3 4 5 6 7 9
=> 13
15 27
15 11 16


'''



def isAvailable(mid):
    bluray = list()
    longest = max(playtime)
    if mid < longest:
        return False
    idx = 0
    length = 0
    for x in playtime:
        if length + x > mid:
            bluray.append(length)
            idx += 1
            length = x
        else:
            length += x
        if idx == m:
            return False

    return True

if __name__ == "__main__":
    n, m = map(int, input().split())
    playtime = list(map(int, input().split()))

    # bluray = list()

    lt = 0
    rt = sum(playtime)
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if isAvailable(mid):
            rt = mid - 1
            res = mid
        else:
            lt = mid + 1



    print(res)






