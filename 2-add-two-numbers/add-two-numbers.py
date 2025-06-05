# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode(0)
        head = dummy
        carry = 0

        while l1 or l2:
            
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            num = l1val + l2val + carry 
            digit = num % 10
            carry = num // 10


            newNode = ListNode(digit)
            head.next = newNode
            head = head.next

            if carry:
                carryNode = ListNode(carry)
                head.next = carryNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
            



