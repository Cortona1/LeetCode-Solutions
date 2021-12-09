# Author: Anthony Corton
# Date: 8/19/2021
# Description: Practicing leetcode problem #27 the topic being remove all
# instances of a specific value from an array


class Solution:
    def removeElement(self, nums, val: int) -> int:
        while nums.count(val) > 0:
            nums.remove(val)


nums = [3,2,2,3]
val = 3
test =Solution()
test.removeElement(nums,val)
print(nums)