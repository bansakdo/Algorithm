# 2. 전화번호 목록

'''
# 효율성 3,4 시간초과 91.7점
def solution(phone_book):
    answer = True

    for i in range(len(phone_book) - 1):
        size = len(phone_book[i])
        for j in range(len(phone_book)):
            print(size, phone_book[i], phone_book[j][:size])
            if i == j or len(phone_book[j]) <= size:
                continue
            if phone_book[j][:size] == phone_book[i]:
                print(False)
                answer = False
                break
            print()
        if not answer:
            break

    return answer
'''
'''
def solution(phone_book):
    answer = True

    for i in range(len(phone_book) - 1):
        size = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            length = len(phone_book[j])
            if length < size and phone_book[i][:length] == phone_book[j]:
                answer = False
                break
            elif phone_book[j][:size] == phone_book[i]:
                answer = False
                break
        if not answer:
            break

    return answer
'''
'''
def solution(phone_book):
    answer = True

    dic ={} #key,value형태의 딕셔너리이용
    for pNumber in phone_book:
        dic[pNumber] = 1 #key:폰번호 value:1
    for pNumber in phone_book: #각각 폰번호마다 검사
        temp=""
        for num in pNumber: #폰번호를 한글자로 쪼개서 반복문 "243"이면 "2" "4" "3"
            temp += num #쪼갠 숫자를 반복문이 돌아갈 때마다 붙음
            print(temp)
            if temp in dic and temp!=pNumber: #딕셔녀리의 키로 존재하는지 검사
                answer = False
        print()
    return answer
'''
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     print(phoneBook)
#     print(phoneBook[1:])
#     print(zip(phoneBook, phoneBook[1:]))
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         print(p1, p2)
#         if p2.startswith(p1):
#             return False
#     return True

# phone_book.sort()

# 입력1.
# phone_book = ["119", "97674223", "1195524421"]
# => return: False

# 입력2.
# phone_book = ["123","456","789"]
# => return: True

# 입력3.
# phone_book = ["12","123","1235","567","88"]
# => return: False

# 입력4.



# 2회차
'''
def solution(phone_book):
    answer = True
    size = len(phone_book)

    for i in range(size - 1):
        for j in range(i+1, size):
            length = min(len(phone_book[i]), len(phone_book[j]))
            if phone_book[i][:length] == phone_book[j][:length]:
                answer = False
                return answer

    return answer
'''
'''
def solution(phone_book):
    answer = True
    phone = set(phone_book)
    for pNum in phone_book:
        cmp = ""
        for p in pNum:
            cmp += p
            if cmp in phone and cmp != pNum:
                answer = False
                return answer

    return answer
'''

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True




phone_book = ["123","456","789", "1235", "756"]
# => return: False

print(solution(phone_book))

