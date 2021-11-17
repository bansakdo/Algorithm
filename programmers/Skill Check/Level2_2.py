'''

citations = [3, 0, 6, 1, 5]
=> 3





'''

citations = [3, 0, 6, 1, 5, 7, 4, 7, 7]
answer = 0
res = []

length = len(citations)
for i in range(length):
    h = citations[i]
    numOfQuote = 0
    for j in range(length):
        if citations[j] >= h:
            numOfQuote += 1
    # print(h, end=' ')
    res.append([h, numOfQuote, length - numOfQuote])
    if numOfQuote >= h:
        answer = max(h, answer)
    # print()
    # print()
print(*res)
print(answer)