from collections import deque


N = int(input())
cards = deque(x for x in range(1, N + 1))

isPass = False

while len(cards) > 1:
    if isPass:
        cards.append(cards.popleft())
        isPass = False
    else:
        cards.popleft()
        isPass = True

print(cards[0])







