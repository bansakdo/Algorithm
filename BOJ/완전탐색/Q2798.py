

N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)
select = []
max_num = 0

for i in range(len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)):
            tot = cards[i] + cards[j] + cards[k]
            if tot <= M:
                max_num = max(max_num, tot)
print(max_num)

