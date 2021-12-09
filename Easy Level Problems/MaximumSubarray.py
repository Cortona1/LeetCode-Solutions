# Author: Anthony Corton
# Date: 8/20/2021
# Description: Practicing leetcode problem #53 the topic find the contiguous
# subarray containing at least one number which has the largest sum and return
# its sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sub_array = 0
        sum_value = 0

        for i in range(len(nums)):
            if i > 0:

                if nums[i] < 0:
                    if nums[i] + sum_value < 0:
                        if sum_value > max_sub_array:
                            max_sub_array = sum_value
                        sum_value = 0
                    else:
                        sum_value += nums[i]

                elif nums[i] > 0:
                    sum_value += nums[i]
                    if sum_value > max_sub_array:
                        max_sub_array = sum_value

            elif i == 0 and nums[i] > 0:
                sum_value += nums[i]
                max_sub_array += nums[i]

        if max_sub_array == 0:
            max_sub_array = nums[0]
            for i in range(1, len(nums)):
                if nums[i] > max_sub_array:
                    max_sub_array = nums[i]

        return max_sub_array
