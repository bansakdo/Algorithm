


def solution(n, times):
    answer = 0
    times.sort()

    lt = 1
    rt = times[-1] * n

    while lt <= rt:
        mid = (lt + rt) // 2
        v = 0
        for t in times:
            v += mid // t
            if v > n:
                break
        if v >= n:
            rt = mid - 1
            answer = mid
        else:
            lt = mid + 1


    return answer


n = 6
times = [7, 10]   # => 28
# n = 8
# times = [7, 10, 2, 3]   # => 9
# n = 8
# times = [7, 10, 8, 1]   # => 7


print(solution(n, times))

