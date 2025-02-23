"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


1 -> 2 -> 5 -> 6
     3 -> 4 -> x
==================

1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6
     

    flat(1)
    curr = 3
    childNode = 3
    nextNode = 5
    tailNode = 4

        flat(3)
        curr = 4

    1
    2
    3

"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        curr = head
        while curr:

            # if we find child node
            if curr.child:
                nextNode = curr.next
                
                # find tail of child list
                tail = curr.child
                while tail.next:
                    tail = tail.next
            
                # rewire
                curr.next = curr.child
                curr.child.prev = curr
                tail.next = nextNode
                if nextNode:
                    nextNode.prev = tail

                curr.child = None

            curr = curr.next
        return head
                











        