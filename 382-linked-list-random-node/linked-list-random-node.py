# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.curr = head
        

    def getRandom(self) -> int:
        node = self.curr
        count = 0
        pick = -1

        while node:

            count += 1

            if random.randint(1, count) == count:
                pick = node.val

            node = node.next
        return pick


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()