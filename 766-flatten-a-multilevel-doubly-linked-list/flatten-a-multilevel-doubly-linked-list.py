class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None

        def flat(head):
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

                # update iterators
                prev = curr
                curr = curr.next
            return prev
            
        flat(head)
        return head
        
