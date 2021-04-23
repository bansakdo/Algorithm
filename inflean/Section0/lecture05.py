# 반복문을 이용항 문제풀이


n = int(input())
# 1. 1부터 n까지 홀수 출력
for i in range(1, n+1):
    if i % 2 == 1 :
        print(i)

# 2. 1부터 n까지의 합 구하기
sumNum = int(0)
for i in range(1, n+1):
    sumNum += i
print(sumNum)

# 3. n의 약수 출력
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')       # 구분자를 줄바꿈으로 사용하지 않고 띄어쓰기로 사용  


