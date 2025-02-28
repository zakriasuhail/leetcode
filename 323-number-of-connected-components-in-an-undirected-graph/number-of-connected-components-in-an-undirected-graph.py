class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]


        # build graph
        for a, b in edges:
            graph[a].append(b) 
            graph[b].append(a)


        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for child in graph[node]:
                dfs(child)
        
        # traverse graph
        components = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)

        return components







        

        