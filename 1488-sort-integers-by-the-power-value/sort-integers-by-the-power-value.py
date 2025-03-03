"""
pv{


}


pv(3)
    pv(10)
        pv(5)
            pv(16)
                pv(8)
                    pv(4)   
                        pv(2)
                            pv(1)     




"""
class Solution:
    def __init__(self):
        self.pv = {1:0}

    def getPV(self, num):
        if num in self.pv:
            return self.pv[num]

        
        if num % 2:
            x = 3 * num + 1
        else:
            x = num / 2

        self.pv[num] = 1 + self.getPV(x)
        return self.pv[num]
        

        

    def getKth(self, lo: int, hi: int, k: int) -> int:
        heap = []
        
        for num in range(lo, hi + 1):
            pv = self.getPV(num)
            heapq.heappush(heap, (-pv, -num))

            if len(heap) > k:
                heapq.heappop(heap)

        return -heapq.heappop(heap)[1]
        