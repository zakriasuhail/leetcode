"""
observations:
- we can do it layer by layer, starting pos = (x,x) -> (n,n)
- we can map number at each index
[1,2,3]
[4,5,6]
[7,8,9]

[7,2,1]
[4,5,6]
[9,8,3]

[15,13,2,5]
[14,6,3,1]
[12,8,4,9]
[16,7,10,11]
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left, right = 0, len(matrix) - 1

        while left < right:
            top, bottom = left, right
            for i in range(right - left):
                
                # store top left corner number in temp var
                topLeft = matrix[top][left + i]

                # move bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move temp num to top right
                matrix[top + i][right] = topLeft

            left += 1
            right -= 1



