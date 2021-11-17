
# 내 풀이
# '''
# def solution(citations):
#     answer = len(citations)
#     citations.sort(reverse=True)
#
#     for i, v in enumerate(citations):
#         if v < i+1:
#             answer = i
#             break
#
#     return answer
# '''


# 다른사람 풀이
# '''
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))


    print(list(enumerate(citations, start=1)))
    print(list(map(min, enumerate(citations, start=1))))

    return answer
# '''



''' 68.8
def solution(citations):

    c_arr = sorted(citations, reverse=True)
    h = len(citations) - 1
    print(c_arr)
    while h > 0:
        if c_arr[h] <= 0 or c_arr[h] > len(citations) or c_arr[c_arr[h] - 1] > c_arr[h]:
            h -= 1
        elif c_arr[c_arr[h] - 1] <= c_arr[h]:
            break
    if h == 0:
        return len(c_arr)
    return h+1

'''






citations = [3, 0, 6, 1, 5]
# citations = [4, 3, 0, 6, 1, 5, 6, 1]
# citations = [3, 0, 6, 1, 5, 5, 1, 5]
# citations = [9, 9, 9, 9, 9, 9, 9, 9]
print(solution(citations))