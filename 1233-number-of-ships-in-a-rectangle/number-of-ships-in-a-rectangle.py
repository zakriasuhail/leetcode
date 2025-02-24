# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        if (topRight.x < bottomLeft.x) or (topRight.y < bottomLeft.y):
            return 0 

        if not sea.hasShips(topRight, bottomLeft):
            return 0

        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1

        mid_x = bottomLeft.x + (topRight.x - bottomLeft.x) // 2
        mid_y = bottomLeft.y + (topRight.y - bottomLeft.y) // 2

        # build quadrant points
        q1 = (Point(mid_x , topRight.y), Point(bottomLeft.x, mid_y + 1))
        q2 = (topRight, Point(mid_x + 1, mid_y + 1))
        q3 = (Point(mid_x, mid_y), bottomLeft)
        q4 = (Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))


        return self.countShips(sea, q1[0], q1[1]) + \
                self.countShips(sea, q2[0], q2[1]) + \
                self.countShips(sea, q3[0], q3[1]) + \
                self.countShips(sea, q4[0], q4[1])


