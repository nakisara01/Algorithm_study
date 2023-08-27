# 구현 알고리즘 학습
# 문제: 정수 N이 입력되면 00시 00분 00초까지의 모든 시간 중에서 3이 하나라도 포함되는 모든 경우의 수 구하기 

n=int(input())

cnt=0

for h in range(n+1): # 시간은 60까지 연산할 필요 없이 입력한 값+1(인덱스 값 고려)으로 결과를 도출
    for m in range(60): # 분은 60까지 연산
        for s in range(60): # 초도 60까지 연산
            if str(n) in str(h) + str(m) + str(s): # str으로 표현된 n 값을 h, m, s의 항목 중 하나라도 가지고 있을 경우 cnt를 하나 추가
                cnt+=1
print(cnt)