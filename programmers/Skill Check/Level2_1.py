'''
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
=> [[15, 15], [15, 15], [15, 15]]

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
=> [[22, 22, 11], [36, 28, 18], [29, 20, 14]]

arr1 = [[2, 1], [3, 4], [7, 8]]
arr2 = [[9, 7, 6], [10, 4, 8]]
=> [[28, 18, 20], [67, 37, 50], [143, 81, 106]]

'''


arr1 = [[2, 1], [3, 4], [7, 8]]
arr2 = [[9, 7, 6], [10, 4, 8]]
answer = []

len_row = len(arr1)
len_col = len(arr2[0])

for r in range(len_row):
    row = []
    for c in range(len_col):
        tmp = 0
        for a in range(len(arr2)):
            tmp += arr1[r][a] * arr2[a][c]
        row.append(tmp)
    answer.append(row)

print(*answer)


