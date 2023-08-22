#그리디 알고리즘 학습
#문제: 행렬을 입력 받은 후 행마다 가장 작은 수를 추출해 이들을 비교하고 가장 큰 수를 출력하는 문제

n, m=map(int, input("행과 열을 정의해주세요: ").split()) #행과 열의 개수 입력

max, tmp=0, 0

for i in range(n): #행의 개수인 n 만큼 반복문 반복
    li= list(map(int, input().split())) 
    tmp=min(li) #행 내에서 가장 작은 수를 tmp에 저장
    if tmp>max: #행마다 가장 작은 수를 추출했을 때 이중 가장 큰 수인 max보다 tmp가 큰 경우, max에 tmp 저장
        max=tmp
    # print("현재까지의 가장 큰 수:", max)
print(max)