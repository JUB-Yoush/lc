#!/usr/bin/env python3
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation
:
assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

- check value to the right
- if same, get rid of self
- how to get rid
- change value to _ and swap values till at end of array
- i and j start at 1 (because 0 is always unqiue)
- j searches for the next unique number (when n[i] != n[j])
- when found, place nj at ni and move ni up i
"""


class Solution(object):
    def removeDuplicates(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l


print(Solution.removeDuplicates(None, [1, 1, 2]))
