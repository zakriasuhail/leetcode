class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score
        

    def top(self, K: int) -> int:
        heap = []
        res = 0
        for score in self.scores.values():
            res += score
            heapq.heappush(heap, score)
            if len(heap) > K:
                res -= heap[0]
                heapq.heappop(heap)
        return res
        

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)