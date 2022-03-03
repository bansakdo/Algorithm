

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
numbers = list(map(int, input().split()))

rst = []
dic = {}
for num in cards:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

def binary_search(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if arr[mid] == target:
        return dic.get(arr[mid])
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)

for num in numbers:
    rst.append(binary_search(cards, num, 0, len(cards) - 1))

print(*rst)







