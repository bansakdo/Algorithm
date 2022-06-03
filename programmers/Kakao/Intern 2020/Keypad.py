

def solution(numbers, hand):
    answer = ''
    now = [[3, 0], [3, 2]]

    for num in numbers:
        if num == '*':
            answer += 'L'
            now[0] = [3, 0]
        elif num == '#':
            answer += 'R'
            now[0] = [3, 2]
        else:
            if num == 0:
                num_pos = [3, 1]
            else:
                num_pos = [(num - 1) // 3, (num - 1) % 3]
            if num in [1, 4, 7]:
                answer += 'L'
                now[0] = num_pos
            elif num in [3, 6, 9]:
                answer += 'R'
                now[1] = num_pos
            else:
                L_dis = abs(now[0][0] - num_pos[0]) + abs(now[0][1] - num_pos[1])
                R_dis = abs(now[1][0] - num_pos[0]) + abs(now[1][1] - num_pos[1])
                if L_dis > R_dis or (L_dis == R_dis and hand == "right"):
                    answer += "R"
                    now[1] = num_pos
                elif L_dis < R_dis or (L_dis == R_dis and hand == "left"):
                    answer += "L"
                    now[0] = num_pos

    return answer



numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))