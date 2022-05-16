# 841
from typing import List


def dfs(start, rooms, visited):
    visited[start] = 1
    for key in rooms[start]:
        if visited[key] == 0:
            dfs(key, rooms, visited)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = [0]*len(rooms)

        dfs(0, rooms, visited)

        for i in range(0, len(rooms)):
            if visited[i] == 0:
                return False

        return True


c = Solution()
res = c.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
print(res)

res = c.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
print(res)


# res = c.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
# print(res)

