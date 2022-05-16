from collections  import defaultdict

#Problem Code: EVEDG


def get_articulation_points(graph, node, parent,  depth, visited,  lowpoint):
    visited[node]=True
    depth[node] = depth[parent]+1
    lowpoint[node] = depth[i]
    child_count = 0
    isArticulation = False
    ret = []
    for child in graph[node]:
        if visited[node]:
            ret = get_articulation_points(graph, child, node,depth, visited, lowpoint)
            child_count += 1
            if lowpoint[child] >= depth[node]:
                isArticulation = True
            lowpoint[node] = min(lowpoint[child], lowpoint[node])

        elif child != parent:
            lowpoint[node] = min(lowpoint[node], depth[child])

    if (parent is not None and isArticulation) or (parent is None and child_count > 1):
        ret.append(node)

    return ret


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n_and_m = input().split()

        n = int(n_and_m[0])

        m = int(n_and_m[1])

        graph = defaultdict(list)
        visited = [0] * n
        depth = [0]*n
        lowpoint = [0]*n
        nodes = list(range(1, n+1))
        print('nodes:', nodes)
        for _ in range(m):
            nodes = list(map(int, input().split()))

            i = nodes[0]
            j = nodes[1]

            graph[i].append(j)
            graph[j].append(i)

        print(graph)
        res = 0
        for k in range(1, n+1):
            if visited[k] is False:
                res += 1
                ret = get_articulation_points(graph, k, None, depth, visited, lowpoint)
                sub = [item for item in nodes if item not in ret and visited[item] is True]
                if len(sub) == 0:
                    res

        print(ret)