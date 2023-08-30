# Exceeds time limit, need to revise

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        return self.step(n,1) + self.step(n,2)
    

    def step(self,remainingSteps,stepSize):
        remainingSteps -= stepSize
        if remainingSteps < 0:
            return 0
        if remainingSteps == 0:
            return 1
        
        return self.step(remainingSteps,1) + self.step(remainingSteps,2)
