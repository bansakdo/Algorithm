# 반복문 (for, while)

# a = range(1, 11)  # 1~10
# print(list(a))

# for i in range(3):      # 0, 1, 2
#     print(i)
#     print("hello")

# for i in range(10, 0, -2):      # 10부터 0까지 -2씩
#     print(i)


# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# i = 10
# while i >= 1 :
#     print(i)
#     i -= 2


# i = 1
# while True:
#     print(i)
#     if i == 10:
#         break
#     i += 1


# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)


for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:                   # for-else 에서 else는 for가 break되지 않고 정상 종료 되었을 때만 실행
    print(11)