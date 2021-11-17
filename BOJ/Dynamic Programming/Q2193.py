
N = int(input())

arr = [1, 1, 2, 3]
if N <= len(arr):
    print(arr[N-1])
else:
    for _ in range(N-len(arr)):
        arr.append(arr[-1] + arr[-2])
    print(arr[-1])
