"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        currSum = 0
        for node in tree:
            currSum += node.val
            for child in node.children:
                currSum -= child.val
            
        for node in tree:
            if currSum == node.val:
                return node
        