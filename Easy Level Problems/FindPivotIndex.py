# Author: Anthony Corton
# Date: 01/2/2022
# Description: Practicing leetcode problem #724 Find Pivot Index
# easy problem asked by microsoft given an array of integers calculate
# pivot index which is where the sum of all numbers strictly on either side
# is equal to zero.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1



