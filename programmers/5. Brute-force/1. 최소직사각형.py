

def solution(sizes):
    width = 1
    height = 1
    for i in range(len(sizes)):
        w, h = sorted(sizes[i])
        width = max(w, width)
        height = max(h, height)

    return width * height


# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(sizes))