import sys

sys.stdin = open("input.txt", "rt")


# 11번 문제. 최대 점수 구하기(knapsack algorithm)

# 내 풀이

# 9번 냅색 문제 참고해서 품
'''
dy에서 시간이 얼마나 지남에 따라 가질 수 있는 최대 점수 저장.
dy[j] = max(dy[j], dy[j - t] + s) 에서 j는 시간, dy[j]는 시간이 j일 때의 최대점수.
max 안의 dy[j]는 다른 문제를 풀어서 시간이 j가 되었을 때의 점수. 
dy[j - t] + s는 해당 문제를 풀어서 시간이 j가 되었을 때의 점수.
둘 중 높은것을 dy[j]에 저장.
j가 t부터 m까지 반복하는 이유는 해당 문제 푸는 시간이 t 만큼 걸리므로, 최소 t 부터 시작.
문제들을 고려하면 언제든 해당 문제를 풀수 있지만 m 이후가 될 수는 없다.
마지막에 dy[m]을 출력하는 이유는 문제가 시간이 m일 경우에 최대 점수를 구하는 것이기 때문.   

'''

# 실패
'''
if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0] * (m+1)

    for i in range(n):
        s, t = map(int, input().split())        # 점수, 시간
        for j in range(t, m+1):
            dy[j] = max(dy[j], dy[j - t] + s)

    print(dy[m])
'''


# 해설
'''
dy를 2차원 리스트로 만듦. n이 5이고 m이 20. (n+1) x m 리스트.
dy[i][j]에서 j는 시간, i는 확인된 문제의 번호. dy[i][j]는 i번 문제까지 확인했고 남은 시간은 j일 때 얻을 수 있는 최대 점수 
문제를 1개씩만 풀 수 있기 때문에 2차원 리스트로 만듦.


dy를 1차원으로 하여 진핸하는 방법 또한 있음
그건 dy에서 뒤부터 접근하는 방법.
기존은 j부터 끝까지 뺐다면 이번엔 마지막부터 j까지.
dy는 미리 0으로 모두 초기화 해 준 후에 m번째 부터 pt까지 -1씩 줄어들며 적용 
dy[j] = max(dy[j], dy[j-pt]) 
dy[j-pt]는 해당 문제를 풀기 전 점수

'''

if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0] * (m+1)
    for i in range(n):
        ps, pt = map(int, input().split())
        for j in range(m, pt-1, -1):            # j는 m부터 pt까지 -1씩 감소
            dy[j] = max(dy[j], dy[j - pt] + ps)

    print(dy[m])
