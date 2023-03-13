import heapq
import itertools

def solution(operations):
    heap = []
    for op in operations:
        c, num = op.split()
        num = int(num)
        if c == "I":
            heapq.heappush(heap, num)
        else:
            if len(heap) == 0:
                continue
            elif num == 1:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
            else:
                heapq.heappop(heap)

    if len(heap) > 0:
        min_num = heap[0]
        max_num = heapq.nlargest(len(heap), heap)[0]
    else:
        min_num, max_num = 0, 0

    return [max_num, min_num]




operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))