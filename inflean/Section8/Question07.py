import sys

sys.stdin = open("input.txt", "rt")

# 7번 문제. 알리바바와 40인의 도둑 (Bottom-Up)

# 내 풀이 (실패)
'''
n = int(input())
bridge = [list(map(int, input().split())) for _ in range(n)]
energy = [0] * (n+1)
# energy = 2147000000
energy[0] = bridge[0][0]
energy[1] = energy[0] + bridge[1][:2]
# energy[0] = 1
cnt = [0] * (n+1)

path = [(0, 0)]


# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

for i in range(2, n*n):
'''


# 해설
'''
최단거리로 가야하기 때문에, 항상 오른쪽 혹은 아래로만 이동
bottom up은 작은 단위에서 키우는 방식
dy[i][j]는 (0, 0)에서 (i, j)까지 가는 최소 비용
맨 처음에 0행과 0열의 모든 dy값을 미리 구해놓는다.
그 다음에 (1, 1)부터 / 방향 대각선 순서로 구한다.


dy[0][0] = 3
dy[0][1] = dy[0][0] + 3 = 6
dy[0][2] = dy[0][1] + 5 = 11
dy[1][0] = dy[0][0] + 2 = 5
dy[2][0] = dy[1][0] + 6 = 11

dy[1][1]을 구할 때에는 dy[0][1]과 dy[1][0] 중 더 낮은값을 더한다.
dy[1][1] = dy[1][0] + 3 = 8
dy[1][2] = dy[1][1] + 4 = 12
dy[2][1] = dy[1][1] + 5 = 13
dy[2][2] = dy[1][2] + 2 = 14

'''

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    dy[0][0] = arr[0][0]

    for i in range(n):
        dy[0][i] = dy[0][i-1] + arr[0][i]
        dy[i][0] = dy[i-1][0] + arr[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]

    print(dy[n-1][n-1])



