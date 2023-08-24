class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # add to set
        # loop thru array
        # check if num + 1 exists in the set
        # if so add to score count
        # if score ends up being larger then the previous max replace it

        numsSet = set(nums)
        checked = set()
        hiScore = 0
        # loop thru array 
        for i,num in enumerate(nums):
            # check if this number has already been in a combo (you can't be in more than one combo)
            if (num in checked) == False:
                # if new, start a new combo meter and add the current number to the checked set
                score = 1
                checked.add(num)
                nextNum = num + 1
                # check if the next number is in the list
                while nextNum in numsSet:
                    checked.add(nextNum)
                    nextNum += 1
                    score += 1
                hiScore = max(score,hiScore)
        return hiScore

