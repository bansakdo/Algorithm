




def solution(s):

    num = 0
    for c in s:
        if c == "(":
            num += 1
        else:
            num -= 1
            if num < 0:
                break

    return True if num == 0 else False




s = "(()))()"
print(solution(s))