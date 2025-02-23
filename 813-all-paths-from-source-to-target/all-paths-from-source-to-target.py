class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        res = []


        def dfs(path, curr):
            nonlocal res

            # base cases
            if curr == len(graph) - 1:
                res.append(path[:])
                return

            # recursive case
            for node in graph[curr]:
                path.append(node)
                dfs(path, node)
                path.pop()

        dfs([0], 0)
        return res













        