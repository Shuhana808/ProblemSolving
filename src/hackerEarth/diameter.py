#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


def dfs(graph, start,height=0, path=[],d={}):
    path = path + [start]
    d[start]=height

    max_di=height
    max_di_path=path
    for node in graph[start]:
        if node not in path:
            weight=graph[start][node]
            di, newpath = dfs(graph, node, height+weight, path)
            if di>max_di:
                max_di=di
                max_di_path=newpath

    return max_di, max_di_path


def calc_diameter(graph):

    max_di, max_di_path=dfs(graph,1)
    diam, path=dfs(graph,max_di_path[len(max_di_path)-1])

    return diam, path


def min_edges(graph,k,com_path=[]):
    diam, path=calc_diameter(graph)
    ret={}
    if diam > k:
        w=0
        i=0
        while i < len(path)-1:
            a=path[i]
            b=path[i+1]
            w=w+graph[a][b]

            if w > k:
                if i == len(path)-2:
                    for k in range(len(com_path)-1,1,-1):
                        if com_path[k] in path :
                            index=path.index(com_path[k])
                            if com_path[k-1]==path[index-1]:
                                ret[com_path[k]]=com_path[k-1]



                else:
                    new_graph = {k: v for k, v in graph.items()}
                    for j in new_graph[b]:
                        if j != a:
                            new_graph[j].pop(b)
                            new_graph[b].pop(j)

                    print(new_graph)
                    edges = min_edges(new_graph,k,com_path)
                    for k, v in edges.items():
                        ret[k]=v

    return ret


if __name__ == '__main__':

    n_and_k = input().split()

    n = int(n_and_k[0])

    k = int(n_and_k[1])

    # arr = list(map(int, input().rstrip().split()))

    edges = []
    graph = defaultdict(dict)

    for _ in range(n - 1):
        edge=list(map(int, input().rstrip().split()))
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]

    diam, path = calc_diameter(graph)
    print(diam,path)
    print(graph)

    # res = maxSubsetSum(arr)


