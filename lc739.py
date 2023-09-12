class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        output = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t >   stack[-1][0]: # is this temp greater then the top of the stack?
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd) # return the # of days it took to find a greater temperature
            stack.append([t,i]) # add the tempurature and index
        return res
        

