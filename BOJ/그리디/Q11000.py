import heapq

N = int(input())
lessons = [list(map(int, input().split())) for _ in range(N)]
lessons.sort()
_in_lesson = []     # 수업의 끝시간
max_classroom = 0

for lesson in lessons:
    if not _in_lesson:
        heapq.heappush(_in_lesson, lesson[1])
    elif any(lesson[0] <= t for t in _in_lesson):
        while _in_lesson and _in_lesson[0] <= lesson[0]:
            heapq.heappop(_in_lesson)
        heapq.heappush(_in_lesson, lesson[1])

    max_classroom = max(max_classroom, len(_in_lesson))


print(max_classroom)



'''
3
1 3
2 4
3 5

=> 2


5
1 4
2 4
3 4
4 6
3 7

=> 4


6
1 2
2 3
3 4
4 5
5 6
6 7

=> 1


6
1 10
2 9
3 7
4 6
5 9
6 9

=> 6

10
1 20000
100 200000
400 1000
500 2000
1100 2000
2000 3000
2500 10000
3000 20000
4000 5000
4500 5000

=> 6

'''