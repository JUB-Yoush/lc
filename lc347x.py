# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

