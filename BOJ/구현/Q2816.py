

# class Node:
#     def __init__(self, data, next=None):



N = int(input())
arr = list(input() for _ in range(N))
cmdList = []

global idx1, idx2, now
idx1, idx2, now = arr.index("KBS1"), arr.index("KBS2"), 0

def move(cmd):
    global now, idx2, idx1
    if cmd == 1:
        if now == N - 1:
            return
        now += 1
        cmdList.append(cmd)
    elif cmd == 2:
        if now == 0:
            return
        now -= 1
        cmdList.append(cmd)
    elif cmd == 3:
        if now == N - 1:
            return
        if now == idx1:
            idx1 += 1
        elif now + 1 == idx1:
            idx1 -= 1
        if now == idx2:
            idx2 += 1
        elif now + 1 == idx2:
            idx2 -= 1
        arr[now], arr[now + 1] = arr[now + 1], arr[now]
        now += 1
        cmdList.append(cmd)
    elif cmd == 4:
        if now == 0:
            return
        if now == idx1:
            idx1 -= 1
        elif now - 1 == idx1:
            idx1 += 1
        if now == idx2:
            idx2 -= 1
        elif now - 1 == idx2:
            idx2 += 1
        arr[now], arr[now - 1] = arr[now - 1], arr[now]
        now -= 1
        cmdList.append(cmd)
    # print(str(cmd) + " - " + str(now) + ": " + " ".join(arr))



while(idx1 != 0 or idx2 != 1):
    if (idx1 < idx2):
        while(now < idx1):
            move(3)
        if (idx1 == 0 and idx2 == 1):
            break
        move(2)
        while(now > 0):
            move(4)
        if (idx1 == 0 and idx2 == 1):
            break
        move(1)
        while(now < idx2):
            move(3)
        if (idx1 == 0 and idx2 == 1):
            break
        move(2)
        while(now > 1):
            move(4)
    else:
        if idx1 == 1 and idx2 == 0:
            move(3)
            break
        while(now < idx2):
            move(3)
        if (idx1 == 0 and idx2 == 1):
            break
        move(2)
        while(now > 0):
            move(4)
        if (idx1 == 0 and idx2 == 1):
            break
        move(1)
        while(now < idx1):
            move(3)
        if (idx1 == 0 and idx2 == 1):
            break
        move(2)
        while(now > 0):
            move(4)

cmdStr = "".join(map(str, cmdList))
while ("21" in cmdStr or "12" in cmdStr):
    cmdStr = cmdStr.replace("12", "")
    cmdStr = cmdStr.replace("21", "")
print(cmdStr)




