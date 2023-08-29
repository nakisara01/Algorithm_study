# DFS/BFS 알고리즘 학습
# Queue 개념 정리, 실습

from collections import deque
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.pop()
queue.append(1)
queue.append(4)
queue.pop()

print(queue)
queue.reverse()
print(queue)