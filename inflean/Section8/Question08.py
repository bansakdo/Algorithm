import sys

sys.stdin = open("input.txt", "rt")

# 8번 문제. 알리바밥와 40인의 도둑 (Top-down)


# 내 풀이


# 해설 듣다 풀음
'''
def DFS(x, y):
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        nx = x - 1
        ny = y - 1
        if nx < 0:
            return DFS(x, ny) + arr[x][y]
        elif ny < 0:
            return DFS(nx, y) + arr[x][y]
        else:
            if arr[x][ny] < arr[nx][y]:
                return DFS(x, ny) + arr[x][y]
            else:
                return DFS(nx, y) + arr[x][y]


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(DFS(n-1, n-1))
'''


# 해설
'''
Top-down 방식은 재귀를 사용
DFS(2, 2) 는 (0, 0)부터 (2, 2)까지의 최소 거리 비용 리턴
DFS(2, 2)는 DFS(2, 1)과 DFS(1, 2)중 더 작은 값에 자신의 arr값을 더한 후 리턴.
이미 구한 값을 여러번 구하는 것을 방지하기 위해 dy값에 저장하여 여러번 호출하는 것 방지. => 위에서 푼거에 적용 안되어 있음.
'''

def DFS(x, y):
    if dy[x][y] > 0:            # 메모이제이션
        return dy[x][y]
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if y == 0:
            dy[x][y] = DFS(x-1, y) + arr[x][y]
        elif x == 0:
            dy[x][y] = DFS(x, y-1) + arr[x][y]
        else:
            dy[x][y] = min(DFS(x-1, y), DFS(x, y-1)) + arr[x][y]
        return dy[x][y]

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    print(DFS(n-1, n-1))
