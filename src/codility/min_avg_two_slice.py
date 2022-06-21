# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys


def solution(A):
    # write your code in Python 3.6
    n = len(A)
    s = []
    s[0] = A[0]
    for i in range(1, n):
        s.append(s[i - 1] + A[i])

    i = 0;
    j = 1
    p = 0;
    q = 0
    min_avg = sys.maxint

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            avg = (s[j] - s[i]) / (j - i + 1)
            if avg < min_avg:
                min_avg = avg
                p = i
                q = j

    return p


print("3\""+"\n")
print('124'.isdigit())
HttpResponseNotAllowed