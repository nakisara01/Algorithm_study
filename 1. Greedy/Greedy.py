    #그리디 알고리즘 학습
#문제: 1,260원의 거스름돈을 걸러주어야할 때 500, 100, 50, 10원짜리 동전이 있다면 거슬러 줘야 할 동전의 최소 개수를 구하라.

change=1260 #거스름돈의 총 금액
cnt=0 #동전 각각의 개수

coin_type=[500,100,50,10] #동전 종류 별 리스트 선언

for coin in coin_type: #coin이라는 변수에 대해 coin_type리스트 만큼 반복
    cnt += change//coin #coin으로 change를 나누었을 때의 몫을 cnt에 더함
    change %= coin #coin에서 change를 나눈 값의 나머지를 change에 저장

print(cnt) #cnt 출력