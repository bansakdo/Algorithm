

def dfs(k, dungeouns, chk):
    if all(chk[i] >= 0 for i in range(len(chk))):
        return sum(chk)

    rst = 0
    for i in range(len(chk)):
        if chk[i] == -1:
            if dungeouns[i][0] <= k:
                chk[i] = 1
                rst = max(rst, dfs(k - dungeouns[i][1], dungeouns, chk))
            else:
                chk[i] = 0
                rst = max(rst, dfs(k, dungeouns, chk))
            chk[i] = -1
    return rst

def solution(k, dungeons):
    chk = [-1] * len(dungeons)
    return dfs(k, dungeons, chk)


k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))