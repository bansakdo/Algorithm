import sys

sys.stdin = open("input.txt", "rt")

# 3번 문제. 후위표기실 만들기

# 실패
'''
m = input()
operation = []
res = ""
second = False
op = ['+', '-', '*', '/', '(', ')']
depth = 1
for i in range(len(m)):
    if not op.__contains__(m[i]):               # 숫자
        res += m[i]
        if operation[-1] == '*' or operation[-1] == '/':
            while True:
                res += operation.pop()
                if not operation[-1] == '*' and not operation[-1] == '/':
                    break
        else:
            res += operation.pop()
    elif m[i] == '(':
        depth += 1
    elif m[i] == ')':
        depth -= 1
        res += operation.pop()
    else:
        operation.append(m[i])
        second = True
    print(operation)
    print(res)
'''

# 방법 들은 후 (실패)
# '''
m = input()
operation = []
res = ""
op = ['+', '-', '*', '/', '(', ')']
start = 0
for x in m:
    if not op.__contains__(x):
        res += x
    elif x == '*' or x == '/':
        if len(operation) == 0 or operation[-1] == '(' or operation[-1] == '+' or operation[-1] == '-':
            operation.append(x)
        elif operation[-1] == '*' or operation[-1] == '/':
            res += operation.pop()
            operation.append(x)
    elif x == '+' or x == '-':
        if operation[start:].__contains__('*'):
            idx = operation.index('*', start)
            operation.insert(idx, x)
        elif operation[start:].__contains__('/'):
            idx = operation.index('/', start)
            operation.insert(idx, x)
        else:
            operation.append(x)
    elif x == '(':
        operation.append(x)
        start = len(operation) - 1
    elif x == ')':
        while True:
            y = operation.pop()
            if y == '(':
                for j in range(len(operation)):
                    if operation[len(operation) - j - 1] == '(':
                        start = len(operation) - j - 1
                else:
                    start = 0
                if len(operation) != 0:
                    res += operation.pop()
                break
            else:
                res += y
else:
    while len(operation) != 0:
        res += operation.pop()
print(res)
# '''

# 해설
'''
a = input()
stack = []
res = ''
for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)
'''

