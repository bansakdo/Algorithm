import sys
import copy

sys.stdin = open("input.txt", "rt")

# 13번 문제. 회장 뽑기(플로이드 워샬 응용)

# 내 풀이
'''
2차 리스트 표를 만들어서 한 사람이 다른 사람에게 가는 최소 경로의 최댓값을 점수로 한다.
'''
'''
n = int(input())
relation = [[100] * (n+1) for _ in range(n+1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    else:
        relation[a][b] = relation[b][a] = 1

# score = copy.deepcopy(relation)
score = [[0] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    print(relation[i])

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            else:
                relation[i][j] = min(relation[i][j], relation[i][k] + relation[k][j])
                # r = relation[i][k] + score[k][j]
                # if score[i][j] == 0:
                #     if relation[i][j] == 0 and score[k][j] >= 1:
                #         score[i][j] = relation[i][k] + score[k][j]
                #         score[j][i] = relation[i][k] + score[k][j]
                #     else:
                #         score[i][j] = relation[i][j]
                #         score[j][i] = relation[i][j]
                # else:
                #     if r != 0:
                #         score[i][j] = max(score[i][j], r)
                #         score[j][i] = max(score[i][j], r)
                # print(i, j, k, r, score[i][j])

    print()
    for i in range(n+1):
        print(relation[i])
    print()

'''




# 해설
'''
입력을 그래프로 일단 그림. 모든 회원의 가까움의 정도를 2차리스트로 만듦.


플로이드 와샬을 했을 때 결과값
0 1 2 2 3
1 0 1 1 2
2 1 0 1 1
2 1 1 0 1
3 2 1 1 0
'''
# '''
if __name__ == "__main__":
    n = int(input())
    dis = [[100] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dis[i][i] = 0
    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        dis[a][b] = 1
        dis[b][a] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         print(dis[i][j], end=' ')
    #     print()

    res = [0] * (n+1)
    score = 100
    for i in range(1, n+1):
        for j in range(1, n+1):
            res[i] = max(res[i], dis[i][j])
        score = min(score, res[i])

    out = []
    for i in range(1, n+1):
        if res[i] == score:
            out.append(i)

    print("%d %d" %(score, len(out)))
    for x in out:
        print(x, end=' ')
# '''



