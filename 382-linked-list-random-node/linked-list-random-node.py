# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nodes = 0
        self.map = {}

        curr = head
        while curr:
            self.map[self.nodes] = curr.val
            self.nodes += 1
            curr = curr.next

        

    def getRandom(self) -> int:
        return self.map[random.randint(0, self.nodes - 1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()