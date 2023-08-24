class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # have left pointer and right pointer
        # if sum is too small l+1
        # if sum is too big then r-1
        # if sum is target then return l+1 and r+1

        l = 0
        r = len(numbers) -1
        found = False
        while (found != True):
            if numbers[l] + numbers[r] > target: r-=1
            elif numbers[l] + numbers[r] < target: l+=1
            elif numbers[l] + numbers[r] == target: return[l+1,r+1]

        