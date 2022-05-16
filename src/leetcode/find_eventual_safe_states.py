from collections import defaultdict

import heapq as hq
from icecream import ic




class Solution:
    def dfs(self, graph, node, visited):
        if visited[node] == 2:
            return False
        elif visited[node] == 1:
            return True

        visited[node] = 1
        is_cycle = False

        for nei in graph[node]:
            is_cycle = is_cycle or self.dfs(graph, nei, visited)

        if not is_cycle:
            visited[node] = 2


        return  is_cycle

    def eventualSafeNodes(self, graph: list) -> list:
        visited = defaultdict(lambda: 0)
        safe_nodes = []
        for node in range(len(graph)):
            if visited[node] == 0:
                self.dfs(graph, node,visited)

        for node in range(len(graph)):
            if visited[node]==2:
                safe_nodes.append(node)

        return safe_nodes



c = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
ic(graph)
res = c.eventualSafeNodes(graph)
ic(res)

graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
ic(graph)
res = c.eventualSafeNodes(graph)
ic(res)