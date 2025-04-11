class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #create an adj list to store the city and all its direct flights
        adj = [[] for _ in range(n)]
        #create an output list to store the shortest distance from src to other flights
        output = [float('inf') for _ in range(n)]
        output[src] = 0
        
        #add in all the direct flights + their cost into the adj list on the index of the src flights
        for s,d,c in flights:
            adj[s].append((d, c))
        print(adj)

        #the graph is the deque to store the src, num of stops taken till now, cost from src
        graph = deque()
        graph.append((src, -1, 0))

        while graph:
            s, stop, cost = graph.popleft()
            if stop >= k: continue
            for nei, c in adj[s]:
                if c+cost < output[nei]:
                    output[nei] = c+cost
                    
                    graph.append((nei, stop+1, c+cost))
        if output[dst] == float('inf'): return -1
        return output[dst]