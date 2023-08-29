# DFS/BFS 알고리즘 학습
# Recursive function 개념 정리, 실습

# ex 1
def recursive():
    print('this is recursive function')
    recursive()

recursive()

# ex 2 - recursive call
def recursive(i):
    if i==100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다')
    recursive(i+1)
    print(i, '번째 재귀함수를 종료합니다')

recursive(1)

# ex 3 - factorial
def factorial_iterative(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n*factorial_recursive(n-1)

n = int(input())

print(factorial_iterative(n))
print(factorial_recursive(n))