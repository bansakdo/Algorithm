import sys

sys.stdin = open("input.txt", "rt")


def Dsort(lt, rt):
    if lt < rt:
        # 나누는 영역
        mid = (lt + rt) // 2
        Dsort(lt, mid)
        Dsort(mid + 1, rt)

        # 더하는 영역
        # 두 리스트 비교하여 tmp에 담은 후 다시 arr에 넣는다.
        p1 = lt
        p2 = mid + 1
        tmp = []
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1
        if p1 <= mid:           # p2쪽이 먼저 끝난 경우
            tmp += arr[p1:mid + 1]
        if p2 <= rt:
            tmp += arr[p2:rt+1]
        for i in range(len(tmp)):
            arr[lt + i] = tmp[i]



if __name__ == "__main__":
    arr = [23, 11, 45, 36, 15, 67, 33, 21]
    print("Before sort : ", end=' ')
    print(arr)
    Dsort(0, 7)
    print()
    print("After sort : ", end=' ')
    print(arr)

