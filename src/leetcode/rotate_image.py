from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(0, (n // 2 + 1)):
            for j in range(i, n - i - 1):

                pi, pj = i, j
                ni, nj = pj, n - 1 - pi
                temp = matrix[pi][pj]

                for k in range(0, 4):
                    ntemp = matrix[ni][nj]
                    matrix[ni][nj] = temp
                    pi, pj = ni, nj
                    ni, nj = pj, n - 1 - pi
                    temp = ntemp

str = 'ewefg'
str2 = 'wec'
print(str[:-1])
print((set(str2)-set(str)))

y = ['dsd','ada']
print("-".join(y))


print([i.lower() for i in "turing"])

import re
x = [10,20]
x.pop(0)
print(x)

x = 'as'

x[0].upper()
print(x)
print("sdsd TUR".capitalize())

z =set('as  s')
z.add('san')
z.update(set(['p', 'f']))
print(z)

# f = open('ada')

try:
    sd=1
except:
    sd=2
finally:
    sd=2
    print('d')

# f.seek()

a = ['as','as']
print(a[0].upper())