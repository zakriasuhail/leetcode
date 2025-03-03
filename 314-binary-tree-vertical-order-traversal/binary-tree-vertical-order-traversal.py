# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hashmap = defaultdict(list)
        minCol = maxCol = 0


        if not root:
            return []


        queue = deque([(root, 0)])

        while queue:

            for i in range(len(queue)):
                curr, col = queue.popleft()
                hashmap[col].append(curr.val)

                minCol = min(minCol, col)
                maxCol = max(maxCol, col)

                if curr.left: queue.append((curr.left, col - 1))
                if curr.right: queue.append((curr.right, col + 1))
        

        # build res
        res = []
        for row in range(minCol, maxCol + 1):
            res.append(hashmap[row])
        return res


