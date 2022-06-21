
from typing import List


class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

class Solution:

    def build_trie(self, paths):

        root = {}
        for path in paths:
            node = root
            for p in path:
                if p not in node.keys():
                    node[p] = {}
                node = node[p]
        print(root)

        return root

    # def traverse_trie(self,trie):
        

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:

        trie = self.build_trie()



tup = (1,)
print(tup)
