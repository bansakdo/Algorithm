

# 풀이 1

N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()

for num in arr:
    lt, rt = 0, N - 1
    isExist = False

    while lt <= rt:
        mid = (lt + rt) // 2
        if num == A[mid]:
            isExist = True
            print(1)
            break
        elif num > A[mid]:
            lt = mid + 1
        else:
            rt = mid - 1

    if not isExist:
        print(0)




# 풀이 2

# N = int(input())
# A = set(map(int, input().split()))
# M = int(input())
# arr = list(map(int, input().split()))
#
# for num in arr:
#     print(1) if num in A else print(0)