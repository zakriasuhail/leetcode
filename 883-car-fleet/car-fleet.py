"""
pos = [10,8,0,5,3]
spd = [2, 4,1,1,3]

      [1, 1, 12, 7, 4]

(0,1) (3,3) (5,1) (8,4) (10, 2)
        7      7      1        1


"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        grouped = sorted(zip(position,speed), key=lambda x:x[0], reverse=True)
        fleet = 1
        lastTime = (target - grouped[0][0]) / grouped[0][1] 
        
        for pos, spd in grouped[1:]:
            currTime = (target - pos) / spd

            if currTime > lastTime:
                fleet += 1
                lastTime = currTime

        return fleet

    



        
        