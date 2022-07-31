from icecream import ic
#
# class Solution:
#     def mySqrt(self, x: int) -> int:
#
#
#         i=0;j=int(x)
#
#         while j>=i:
#             mid = int((i+j)/2)
#             # ic(i,j,mid)
#             square = mid*mid
#             if square > x:
#                 j = mid-1
#             elif square < x:
#                 i = mid+1
#             elif square == x:
#                 return mid
#
#         return j
#
#
# c = Solution()
# n = 3
# res = c.mySqrt(n)
# ic(n)
# ic(res)


# from typing import List
#
#
# class Solution:
#     def makeBeautiful(self, arr: List[int]) -> List[int]:
#
#         removed = True
#
#         while removed:
#
#             indexes = []
#
#             removed = False
#             i = 0
#             while i < len(arr) - 1:
#                 diff_sign = (arr[i + 1] >= 0) if (arr[i] < 0) else (arr[i + 1] < 0)
#                 if diff_sign:
#                     removed = True
#                     indexes.append(i)
#                     indexes.append(i + 1)
#                     arr.pop(i+1)
#                     arr.pop(i)
#                     print(arr)
#
#                     i = i - 1
#                     if i < 0:
#                         i=0
#
#                 else:
#                     i = i + 1
#             print(arr)
#
#         return arr
#
#
#
#
# c = Solution()
# n = [-145, -69, 56 ,-123, 84 ,76 ,-49 ,-169, -141 ,-173, -79, -71, 82, -87, 162, 182, -73, -151, -95, -195 ,10 ,42 ,24,
#      -171, 184, 44 ,54, -141, 110 ,58 ,186 ,-39 ,-47 ,-69 ,-87 ,148, -111 ,32 ,-189, 92, 32]
#
# # n = [-145  ,-169, -141 ]
#
# # n = [2, 1, -4 ,3 ,-5, 2 ,6, -3]
# res = c.makeBeautiful(n)
# # ic(n)
# ic(res)

import collections
from collections import deque
from collections import defaultdict


class Solution:
    def findNumberOfGoodComponent(self, V, adj):
        visited = [False] * (V + 1)
        adj_list = [0] * (V + 1)

        for i in range(0,V+1):
            adj_list [i] = []

        for e in adj:

            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])

        res = 0
        for v in range(1, V + 1):
            if visited[v] == False:
                visited[v] = True
                s = {v}
                q = deque([])
                good = True

                for u in adj_list[v]:
                    s.add(u)
                    q.append(u)

                while len(q) > 0:
                    u = q.popleft()
                    visited[u] = True
                    s_c = set(adj_list[u])
                    s_c.add(u)
                    if s_c != s:
                        good = False
                    for n in adj_list[u]:
                        # if n not in s:
                        #     good = False
                        if visited[n] == False:
                            q.append(n)
                if good:
                    res += 1
        return res

c = Solution()
V = 4
# adj = [[2,3],[1,3],[1,2]]
adj = [[1,2],[1,3],[1,4]]

res = c.findNumberOfGoodComponent(V,adj)
# ic(n)
ic(res)