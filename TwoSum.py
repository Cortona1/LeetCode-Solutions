# Author: Anthony Corton
# Date: 9/12/2021
# Description: Practicing leetcode problem #1, given an array of integers nums
# and an integer target, return indices of the two numbers that add up to the
# target


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        answer = []

        for number in range(len(nums)):
            for second_number in range(1, len(nums)):
                if nums[number] + nums[second_number] == target and number != second_number:
                    answer.append(number)
                    answer.append(second_number)
                    return answer