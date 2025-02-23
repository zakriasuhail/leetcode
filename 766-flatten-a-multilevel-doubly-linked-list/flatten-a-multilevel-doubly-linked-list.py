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
        def flat(head):
            if not head: 
                return None
            
            curr = head
            prev = None
            while curr:
                
                # process sublist
                if curr.child:
                    childNode = curr.child
                    nextNode = curr.next
                    
                    # rewire current node
                    curr.next = childNode
                    childNode.prev = curr
                    
                    # get and rewire tail
                    tailNode = flat(childNode)
                    if tailNode and nextNode:
                        tailNode.next = nextNode
                        nextNode.prev = tailNode

                    # set child to None
                    curr.child = None

                prev = curr
                curr = curr.next
            return prev
            
        flat(head)
        return head
        