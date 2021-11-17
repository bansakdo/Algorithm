'''



'''



from collections import deque
# 내 풀이. 큐 사용.
# '''
def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        now = prices.popleft()
        time = len(prices)
        for x in enumerate(prices):
            if x[1] < now:
                time = x[0] + 1
                break
        answer.append(time)

    return answer
# '''

# 다른사람 풀이. 스택 사용
''' 
def solution(p):
    ans = [0] * len(p)
    stack = [0]
    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
    return ans
'''

# prices = [1, 2, 3, 2, 3]
prices = [1, 2, 3, 2, 2, 3, 1]

print(solution(prices))