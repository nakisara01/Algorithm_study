# 구현 알고리즘 학습
# 문제: 정수 N이 입력되면 00시 00분 00초까지의 모든 시간 중에서 3이 하나라도 포함되는 모든 경우의 수 구하기 

n=int(input())

cnt=0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt+=1
print(cnt)