# 구현 알고리즘 학습
# 문제: 나이트는 8*8의 평면 위에서 수평으로 두번, 수직으로 한번 또는 수직으로 두번, 수평으로 한번 움직일 수 있다. 이때 좌표를 입력받았을 때 나이트가 이동할 수 있는 경우의 수를 구하시오.

point = input()
row = int(point[1])
column = ord(point[0])-ord('a')+1 # ord는 문자를 ASCII 코드로 변경해주는 파이썬의 내장함수로 입력받은 값의 알파벳을 아스키코드로 변환해 이를 a로 빼고 1을 더해 순서를 유추하는 방식

# 나이트가 이동할 수 있는 모든 경우의 수 정의
routes = [(-2,-1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]

cnt=0

for route in routes: # routes 안에 있는 요소 하나하나를 route로 사용
    move_row = row+route[0] # 입력받은 row 값에서 route의 x 방향 이동 값을 더해 move_row로 정의
    move_column = column+route[1] # 입력받은 column 값에서 route의 y 방향 이동 값을 더해 move_column으로 정의
    
    # 정의한 move_row와 move_column의 값이 8*8 체스판을 넘어가지 않는지 판단
    if move_row > 0 and move_row < 9 and move_column > 0 and move_column < 9:
        cnt+=1
        
print(cnt)