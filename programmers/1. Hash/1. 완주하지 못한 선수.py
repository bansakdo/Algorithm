# 완주하지 못한 선수
import collections

# 내 풀이
'''
def solution(participant, completion):
    answer = ''
    dic = dict()
    for p in participant:
        dic[p] = dic.get(p, 0) + 1

    for c in completion:
        dic[c] -= 1

    for p in participant:
        if dic[p] == 1:
            answer = p

    return answer
'''

# 추천
# '''
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
# '''

# 입력1.
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
# => return: "leo"

# 입력2.
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]
# => return: "vinko"

# 입력3.
# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]
# => return: "mislav"


print(solution(participant, completion))