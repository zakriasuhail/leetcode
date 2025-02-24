class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged = self.merge(nums1, nums2)

        if len(merged) % 2:
            return merged[len(merged) // 2]
        else:
            return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2




    
    def merge(self, nums1, nums2):
        res = []

        p1 = p2 = 0

        while p1 < len(nums1) or p2 < len(nums2):

            if p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] <= nums2[p2]:
                    res.append(nums1[p1])
                    p1 += 1
                else:
                    res.append(nums2[p2])
                    p2 += 1

            elif p1 < len(nums1):
                res.append(nums1[p1])
                p1 += 1
            
            else:
                res.append(nums2[p2])
                p2 += 1

        return res


        
        