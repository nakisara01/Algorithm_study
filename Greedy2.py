#그리디 알고리즘 학습
#문제: 큰 수의 법칙

n,m,k = map(int, input().split()) # 배열의 크기 n, 숫자가 더해지는 횟수 m, 한 숫자를 여러번 더하는 횟수 k 입력
nums=list(map(int, input().split())) # nums 배열에 요소 입력

nums.sort() # nums의 요소들 오름차순으로 정렬
max=nums[n-1] # nums 배열에서 가장 큰 수 정의
next=nums[n-2] # nums 배열에서 두 번째로 큰 수 정의

cnt, sum= 0, 0

for i in range(m): # sum 구하는 for문 작성 
    if cnt==k: # if문에서 k를 충족했을 때 sum에 두 번째로 큰 수를 더하고 cnt를 0으로 만든다.
        sum+=next
        cnt=0
    else: # sum에 가장 큰 수인 max를 더하고 cnt를 1씩 추가한다.
        sum+=max
        # print(sum)
        cnt+=cnt+1
print(sum)