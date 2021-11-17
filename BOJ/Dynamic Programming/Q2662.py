

N, M = map(int, input().split())
byInvestment = [[0 for _ in range(M + 1)]]

for _ in range(N):
    byInvestment.append(list(map(int, input().split())))

table = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
pos = [[[0 for _ in range(M+1)] for _ in range(M + 1)] for _ in range(N+1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        table[i][j] = max(table[i][j-1], byInvestment[i][j])
        if table[i][j] == byInvestment[i][j]:
            pos[i][j][j] = i
        else:
            pos[i][j] = pos[i][j-1].copy()
        for k in range(1, i+1):
            if table[i][j] < table[k][j-1] + byInvestment[i-k][j]:
                table[i][j] = table[k][j-1] + byInvestment[i-k][j]
                pos[i][j] = pos[k][j-1].copy()
                pos[i][j][j] = i-k

print(table[-1][-1])
print(*pos[-1][-1][1:])



'''
6 3
1 5 1 3
2 6 5 5
3 7 9 7
4 10 15 10
5 13 21 14
6 16 27 19

27
0 6 0

4 3
1 5 1 2
2 6 5 4
3 7 9 11
4 8 15 12

16
1 0 3




'''