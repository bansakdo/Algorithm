import sys
import heapq as hq

sys.stdin = open("input.txt", "rt")

# 2번. 이진트리 순회(깊이 우선탐색)

# list = [1, 2, 3, 4, 5, 6, 7]
# hq.heapify(list)
#
# print(list)


'''
DFS : 깊이 우선 탐색

전위 : 부모 -> 왼쪽자식 -> 오른쪽자식
중위 : 왼쪽자식 -> 부모 -> 오른쪽자식
후위 : 왼쪽자식 -> 오른쪽자식 -> 부모

자식노드 구하기
    왼쪽자식 : 부모 노드 * 2
    오른쪽자식 : 부모 노드 * 2 + 1

'''

def DFS(v):
    if v > 7:
        return
    else:
        # 전위순회
        '''
        print(v, end=' ')
        DFS(v * 2)
        DFS(v * 2 + 1)
        '''
        # 중위순회
        '''
        DFS(v * 2)
        print(v, end=' ')
        DFS(v * 2 + 1)
        '''
        # 후위순회
        '''
        DFS(v * 2)
        DFS(v * 2 + 1)
        print(v, end=' ')
        '''


if __name__ == "__main__":
    DFS(1)

