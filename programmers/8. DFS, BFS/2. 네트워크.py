
def DFS(idx, ch, computers):
    for i in range(len(computers)):
        if i == idx or ch[i] == 1:
            continue
        elif computers[idx][i] == 1 and ch[i] == 0:
            ch[i] = 1
            DFS(i, ch, computers)

def solution(n, computers):
    answer = 0
    ch = [0] * n
    for i in range(n):
        if ch[i] == 0:
            ch[i] = 1
            answer += 1
            DFS(i, ch, computers)

    return answer



n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# -> 2
print(solution(n, computers))




