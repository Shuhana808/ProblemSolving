# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque
from icecream import ic

def solution(A, B):
    # write your code in Python 3.6
    stack = deque()
    for i in range(len(A) - 1, -1, -1):
        if len(stack) == 0:
            stack.append(i)
        else:
            if B[i] == 0:
                stack.append(i)
            else:
                eaten = False
                while len(stack) > 0:
                    top = stack.pop()
                    # print('top',top)
                    if B[top] == 1:
                        stack.append(top)
                        break
                    else:
                        if A[i] < A[top]:
                            eaten = True
                            stack.append(top)
                            break

                if not eaten:
                    stack.append(i)
    return len(stack)



nums = ([0,1],[1,1])
res = solution([0,1],[1,1])
ic(res)
