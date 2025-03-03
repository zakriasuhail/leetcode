"""
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]


[0,1,2,3,4,5,6,7,8,9,10,11,12]


1
10 11 12 13



"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:


        def dfs(num):
            # base case
            if num <= n:
                res.append(num)

            if len(res) == n + 1:
                return 

            # recursive case
            for i in range(10):
                if num == 0 and i == 0:
                    continue

                newNum = num * 10 + i
                if newNum <= n:
                    dfs(newNum)





        res = []
        dfs(0)
        return res[1:]
        