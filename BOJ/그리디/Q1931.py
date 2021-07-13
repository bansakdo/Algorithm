
n = int(input())

meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x: (x[1], x[0]))
availableMeeting = 0
numOfMeeting = len(meeting)
endTime = meeting[0][0]

for i in range(numOfMeeting):
    if endTime > meeting[i][0]:
        continue

    endTime = meeting[i][1]
    availableMeeting += 1


print(availableMeeting)




