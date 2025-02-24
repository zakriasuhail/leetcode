"""
a b c

a/b = 2, b/a = 1/2

b/c = 3  c/b = 1/3

a b
b c

b x
x a

a x
x a


a/b = 2/3    b/a = 2/3
b/c = 5/2    c/b = 2/5
bc/cd = 5/1  cd/bc = 1/5


b . c
-----
c . d


"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:


        


        graph = defaultdict(defaultdict)


        def bt(curr, target, prod, visited):
            visited.add(curr)
            ret = -1.0

            if target in graph[curr]:
                ret = prod * graph[curr][target]
            else:
                for num, val in graph[curr].items():
                    if num in visited:
                        continue
                    ret = bt(num, target, prod * val, visited)
                    if ret != -1.0:
                        break
            visited.remove(curr)
            return ret
                    

            



        for i in range(len(equations)):
            x, y = equations[i]
            value = values[i]
            graph[x][y] = value
            graph[y][x] = 1 / value

        res = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ret = -1.0

            elif dividend == divisor:
                ret = 1.0

            else:
                visited = set()
                ret = bt(dividend, divisor, 1, set())

            res.append(ret)
        return res
            
            


            



        





        