#https://leetcode.com/problems/combination-sum/
"""
what is the thinking process for adding numbers?
because the system otherwise is fairly simple:
- pick a number + add to current sum
- if current sum == target: check if combination already exists in hash
- if dont exist then add
- continute until every option exausted
- so start with an empty list
- make the decision to add [] or that number
- but you can add numbers repeatedly so when do you... stop adding that number
- [], current number, or move to next number
- three branches instead of two?
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pass