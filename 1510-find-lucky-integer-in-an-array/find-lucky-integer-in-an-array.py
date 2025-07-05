class Solution:
    def findLucky(self, arr: List[int]) -> int:

        counter = collections.Counter(arr)
        top = -1
        for num, freq in counter.items():
            if num == freq:
                top = max(top, num)
        return top

        