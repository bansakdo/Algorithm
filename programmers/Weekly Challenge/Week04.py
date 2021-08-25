


def solution(table, languages, preference):

    prefer = {lang: pref for lang, pref in zip(languages, preference)}
    scores = dict()
    for t in table:
        t_item = t.split(' ')
        job = t_item[0]
        for i in range(1, 6):
            if t_item[i] in languages:
                score = scores.get(job, 0) + prefer[t_item[i]] * (6 - i)
                scores[job] = score

    return sorted(scores.items(), key=lambda x: (-x[1], x[0]))[0][0]




table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
print(solution(table, languages, preference))       # "HARDWARE"

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table, languages, preference))       # "PORTAL"