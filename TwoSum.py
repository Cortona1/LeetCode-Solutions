# Author: Anthony Corton
# Date: 9/12/2021
# Description: Practicing leetcode problem #1, given an array of integers nums
# and an integer target, return indices of the two numbers that add up to the
# target


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 2:
            return [0, 1]

        previous_values = {}

        for index, value in enumerate(nums):
            target_value = target - value

            if index != 0:
                needed_index = previous_values.get(target_value)
                if needed_index is not None:
                    return [index, needed_index]

            previous_values[value] = index

