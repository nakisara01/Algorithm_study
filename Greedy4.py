#그리디 알고리즘 학습
#문제: 어떤 수 n 과 k를 입력받고 1. n에서 1을 빼는 연산 혹은 2. n을 k로 나누는 연산만을 통해서 n을 1로 만든다. 단 2번은 n이 k로 나누어 떨어질 때만 가능하다.
n, k= map(int, input("input n, k: ").split()) #n, k 입력

cnt=0

while True:
    if n==1: #n이 1일 경우 while문 종료
        break
    elif n%k==0: #n이 k로 나누어 떨어질 경우, 나눈 후 몫을 n으로 재정의
        n=n//k
        cnt+=1
    else: #n이 k로 나누어 떨어지지 않으면 n-1후 cnt에 +1
        n-=1
        cnt+=1
print(cnt)