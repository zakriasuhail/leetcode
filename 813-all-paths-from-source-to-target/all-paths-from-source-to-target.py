class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(curr, path):
            
            # base cases
            if curr == dest:
                res.append(path[:])
                return
            # recurse
            for neighbor in graph[curr]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
            

        res = []
        src, dest = 0, len(graph) - 1
        dfs(src, [0])
        return res