"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class NewNode:
    def __init__(self, val, children, parent=None):
        self.val = val
        self.children = children
        self.parent = parent


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':

        hmap = defaultdict(list)
        for node in tree:
            for child in node.children:
                hmap[child] = (1, len(child.children))

        for node in tree:
            if node not in hmap:
                return node
        