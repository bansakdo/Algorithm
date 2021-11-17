
def dfs(_idx, _sum):
    global n, s, arr
    _num = 0
    if _idx == n:
        return 0
    if _sum + arr[_idx] == s:
        _num += 1

    _num += dfs(_idx + 1, _sum)
    _num += dfs(_idx + 1, _sum + arr[_idx])

    return _num

n, s = map(int, input().split())
arr = list(map(int, input().split()))

num = 0
print(dfs(0, 0))
