# 3. 조건문 if(분기, 중첩)

# tab 1번은 공백 4칸
'''
== 같다
!= 같지 않다

'''

x = 7
if x == 7:
    print("Lucky")
    print("ㅋㅋ")

# 중첩 if문
x = 10
if x >= 10:
    if x % 2 == 1:
        print("10 이상의 홀수")

x = 9
if x > 0:
    if x < 10:
        print("10보다 작은 자연수")

x = 7
if x > 0 and x < 10:
    print("10보다 작은 자연수")

x = 7
if 0 < x < 10:
    print("10보다 작은 자연수")

x = 10
if x > 0:
    print("양수")
else:
    print("음수")

x = 93
if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print('C')
elif x >= 60:
    print('D')
else:
    print('F')
