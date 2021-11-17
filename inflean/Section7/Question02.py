import sys

sys.stdin = open("input.txt", "rt")

# 2번 문제. 휴가.


# 내 풀이
'''
def DFS(L, sum):
    global tot
    if L == n and sum > tot:
        tot = sum
    elif L < n:
        day = counsel[L][0]
        # print("\nday:", day)
        # print("whole ch:", ch)
        if 1 not in ch[day[0]:day[1]+1] and day[1] <= n:
            # print("ch:", ch[day[0]:day[1]+1])
            for i in range(day[0], day[1] + 1):
                ch[i] = 1
            DFS(L + 1, sum + counsel[L][2])
            for i in range(day[0], day[1]+1):
                ch[i] = 0
        DFS(L + 1, sum)

if __name__ == "__main__":
    n = int(input())
    counsel = []
    for i in range(n):
        t, p = map(int, input().split())            # time, payment
        start = i + 1
        end = i + t
        counsel.append([[start, end], t, p, round(p/t, 2)])     # 날짜, 소요시간, 금액, 일당
    ch = [0] * (n+1)
    tot = 0
    counsel.sort(reverse=True, key=lambda x: x[3])
    # print(counsel)
    DFS(0, 0)
    print(tot)
'''
'''
상담 일정을 입력받은 후, 하루에 상담비용이 가장 효율이 좋은 순서로 정렬한다.(일당이 높은 순에서 낮은순으로 내림차순)
ch 를 통해 빈 날짜를 확인할 수 있도록 하고
DFS에서 두번째 매개변수인 sum에 통해 현재까지의 금액을 저장.
상담중 일당이 높은 순서로 DFS를 실행, 해당 기간에 상담이 없는지 ch를 통해 확인.(1이 있으면 상담 일정이 있음)
이 상담 말고 다른 것을 여러개 했을 때 더 이득일 수 도 있으므로, 
DFS에서는 해당 상담을 했을때와 안했을 때 두번의 DFS를 호출한다.
DFS의 첫번째 매개변수인 L이 n과 같아지고(모든 일정 확인) sum이 tot보다 커지면 tot에 sum 저장
DFS가 모두 끝나면, tot는 제일 많이 벌었을때 받을 수 있는 금액이다.
'''

# 해설

def DFS(L, sum):
    global res
    if L == n+1:
        if sum > res:
            res = sum
    else:
        if L + T[L] <= n+1:
            DFS(L + T[L], sum + P[L])
        DFS(L + 1, sum)


if __name__ == "__main__":
    n = int(input())
    T = list()
    P = list()
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    T.insert(0, 0)              # index를 날짜로 하기 위해 한칸씩 뒤로 미룸.
    P.insert(0, 0)
    DFS(1, 0)
    print(res)


