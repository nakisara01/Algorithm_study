# 구현 알고리즘 학습
# 문제: L R D U 의 명령어를 통해서 좌표 평면 내에서의 점을 계산

n = int(input())
root = list(map(str, input().split())) # L R D U로 구성된 이동 순서 입력

x,y = 1,1
    
for i in range(len(root)): # 반복문을 이동 순서의 개수 만큼 반복
    if root[i]=='L': # L일 경우 x좌표를 -1
        x-=1
    elif root[i]=='R': # R일 경우 x좌표를 +1
        x+=1
    elif root[i]=='U': # U일 경우 y좌표를 -1
        y-=1
    elif root[i]=='D': # D일 경우 y좌표를 +1
        y+=1
        
    if x<=0 or y<=0: # x 값이나 y 값이 0 이하로 떨어져 좌표평면을 벗어났을 경우 값을 1로 복원하여 재정의
        if x<=0:
            x=1
        elif y<=0:
            y=1
            
    if x>n or y>n: # x 값이나 y 값이 n 이상로 올라가 좌표평면을 벗어났을 경우 값을 n으로 복원하여 재정의
        if x>n:
            x=n
        elif y>n:
            y=n
        
print(x, y)