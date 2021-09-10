

def solution(weights, head2head):
    player = []
    for i, w in enumerate(weights):
        win_num = head2head[i].count("W")
        match_num = len(weights) - head2head[i].count('N')
        winning_rate = win_num / match_num if match_num != 0 else 0
        heavier_winning_num = len([j for j in range(len(weights)) if weights[j] > w and head2head[i][j] == 'W'])
        # 번호, 자신무게, 승리횟수, 더 무거운 선수 승리 횟수
        player.append([i+1, w, winning_rate, heavier_winning_num])

    player.sort(key=lambda x: [-x[2], -x[3], -x[1], [0]])

    return list(zip(*player))[0]


weights = [50,82,75,120]
head2head = ["NLWL","WNLL","LWNW","WWLN"]           # [3,4,1,2]
print(solution(weights, head2head))

weights = [145,92,86]
head2head = ["NLW","WNL","LWN"]                     # [2, 3, 1]
print(solution(weights, head2head))

weights = [60,70,60]
head2head = ["NNN","NNN","NNN"]                     # [2, 1, 3]
print(solution(weights, head2head))

weights = [60,70,60, 80]
head2head = ["NWNL","LNWN","NLNW", "WNLN"]          # [1, 3, 4, 2]
print(solution(weights, head2head))

weights = [60, 70, 60, 80, 90]
head2head = ["NWNLW", "LNWNN", "NLNWL", "WNLNW", "LNWLN"]          # [1, 4, 3, 5, 2]


print(solution(weights, head2head))