import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        a = heapq.heappop(scoville)
        if a >= K:
            break
        answer += 1
        b = heapq.heappop(scoville)
        res = a + 2 * b
        heapq.heappush(scoville, res)
        print(scoville)

    if len(scoville) == 1 and heapq.heappop(scoville) < K:
        answer = -1
    return answer


'''
scoville = [1, 2, 3, 9, 10, 12]
K = 7
=> 2



'''


scoville = [1, 2, 3, 9, 10, 12, 1, 5]
K = 9

print(solution(scoville, K))