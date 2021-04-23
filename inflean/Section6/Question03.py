import sys

sys.stdin = open("input.txt", "rt")

'''
def DFS(x, n):
    if x > n:
        return
    else:
        DFS(x+1, n)
        print(x)




if __name__ == "__main__":
    DFS(1, int(input()))
'''



# 해설
'''
3을 입력했을 경우, 
1이 들어가는 경우와 안들어가는 경우, 
2가 들어가는 경우와 안들어가는 경우,
3가 들어가는 경우와 안들어가는 경우
총 2^3개가 있다.

DFS(1)을 호출하여 1을 넣는 경우와 안넣는경우로 구분.
다음 재귀함수에는 매개변수 다음 숫자 넣어서 실행

이와 같이 루트에서 두가닥씩 긍정,부정으로 뻗어 나가는 것을 상태트리라고 함.

ch 리스트를 사용하여 각 숫자가 사용되는지 안되는지 체크. 1이면 사용, 0이면 사용 안함.



'''


def DFS(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)

if __name__ == "__main__":
    n = int(input())
    ch = [0]*(n+1)
    DFS(1)



