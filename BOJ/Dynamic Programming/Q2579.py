
def dfs(steps, stair, now, last_num):
    if now == last_num - 1:
        return sum([stair[i] for i in steps])

    score = 0
    if not (len(steps) >= 2 and (now + 1 - steps[-1]) == (steps[-1] - steps[-2]) == 1):
        steps.append(now + 1)
        score = dfs(steps, stair, now + 1, last_num)
        steps.pop()
    if now + 2 < last_num:
        steps.append(now + 2)
        score = max(score, dfs(steps, stair, now + 2, last_num))
        steps.pop()
    return score


N = int(input())
stair = list(map(int, [input() for _ in range(N)]))

print(dfs([], stair, -1, N))