# Author: Anthony Corton
# Date: 8/20/2021
# Description: Practicing leetcode problem #35 the topic being search for insert
# position which returns the index if target found and if not returns the next
# close index for where it would be had the target been present.


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = high + low // 2

            if nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

            else:
                return mid

        if mid == 0 and nums[0] > target:    # edge case to handle first index
            return 0

        return mid + 1