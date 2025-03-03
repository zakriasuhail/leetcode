# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []


        queue = deque([root])

        res = []
        flip = False

        while queue:
            
            # traverse by level
            level = deque([])
            for i in range(len(queue)):

                curr = queue.popleft()

                # add to level queue
                if flip:
                    level.appendleft(curr.val)
                else:
                    level.append(curr.val)

                # add children for next level
                for child in [curr.left, curr.right]:
                    if child:
                        queue.append(child)

            res.append(list(level))
            flip = not flip
        return res

                
                

        