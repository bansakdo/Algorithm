

# 내가 푼거
# '''
def solution(genres, plays):
    answer = []
    gen_per_play = {}

    for i in range(len(genres)):
        tmp = gen_per_play.get(genres[i], [])
        tmp.append([i, plays[i]])
        gen_per_play[genres[i]] = tmp
    items = list(gen_per_play.items())
    sum_data = []
    for i in range(len(gen_per_play)):
        item_datas = items[i]
        song_data = item_datas[1]
        sum_data.append([item_datas[0], sum([j[1] for j in song_data])])
    sum_data.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(gen_per_play)):
        genre_data = sorted(gen_per_play[sum_data[i][0]], key=lambda x: x[1], reverse=True)
        answer.append(genre_data[0][0])
        if len(genre_data) >= 2:
            answer.append(genre_data[1][0])

    return answer
# '''

# 다른사람 풀이
'''
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
'''



genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# => [4, 1, 3, 0]

print(solution(genres, plays))