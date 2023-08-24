# 구현 알고리즘 학습
# 문제: L R D U 의 명령어를 통해서 좌표 평면 내에서의 점을 계산

n = int(input())
root = list(map(str, input().split()))

x,y = 1,1
    
for i in range(len(root)):
    print(root[i])
    
    if root[i]=='L':
        x-=1
    elif root[i]=='R':
        x+=1
        print(x)
    elif root[i]=='U':
        y-=1
    elif root[i]=='D':
        y+=1
        
    if x<=0 or y<=0:
        if x<=0:
            x=1
        elif y<=0:
            y=1
            
    if x>n or y>n:
        if x>n:
            x=n
        elif y>n:
            y=n
        
print(x, y)