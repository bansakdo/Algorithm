import sys


sys.stdin = open("input.txt", "rt")

# 9번 문제. 가방문제 (knapsack problem)

# 내 풀이
'''
n, limit = map(int, input().split())
jewel = []
# ch = [0] * n
tot = 0
for _ in range(n):
    weight, worth = map(int, input().split())
    per = round(worth / weight, 2)
    jewel.append([weight, worth, per])

jewel.sort(reverse=True, key=lambda x: x[2])
print(jewel)

for i in range(n):
    if jewel[i][0] < limit:
        # ch[i] = 1
        limit -= jewel[i][0]
        tot += jewel[i][1]
print(tot)
'''
'''
def DFS(k, w):
    global highest, limit
    if limit < 0:
        return
    if k == n or limit == 0:
        print(ch, w, limit)
        if w > highest:
            highest = w
    else:
        num = 0
        DFS(k + 1, w)
        while limit >= jewel[k][0]:
            num += 1
            limit -= jewel[k][0]
            ch.append(jewel[k][0])
            DFS(k + 1, w + num * jewel[k][1])
        limit += num * jewel[k][0]
        for _ in range(num):
            ch.pop()


if __name__ == "__main__":
    n, limit = map(int, input().split())
    jewel = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        jewel[i][0], jewel[i][1] = jewel[i][1], jewel[i][0]
    highest = 0
    ch = []
    print(jewel)

    DFS(0, 0)
    print(highest)
'''



'''

n, limit = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(n)]
dy = [0] * (limit + 1)

for i in range(n):
    v = jewel[i][1]
    k = jewel[i][0]
    for j in range(k, limit + 1):
        if dy[j] < dy[j-k] + v:
            dy[j] = dy[j-k] + v

print(dy[-1])

'''

# 해설
'''
dy 리스트를 모두 0으로 limit + 1 크기만큼 초기화
dy[j]는 j 무게만큼 담았을 때의 최대 가치
다이나믹 프로그래밍은 작은 단위부터 시작..
첫번째 보석 무게가 5, 가치가 12이면
j는 5부터 시작. limit까지.
dy[j] = dy[j - w] + v : 보석 담고 나서 가치 = 현재 보석 담기 전의 가치 + 현재 보석 가치
모든 보석 위와 같이 실행.
 
'''
'''
if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0] * (m+1)
    for i in range(n):
        w, v = map(int, input().split())        # 무게, 가치
        for j in range(w, m+1):
            dy[j] = max(dy[j], dy[j-w] + v)


    print(dy[m])
'''