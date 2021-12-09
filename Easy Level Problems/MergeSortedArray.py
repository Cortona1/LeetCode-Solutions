# Author: Anthony Corton
# Date: 8/27/2021
# Description: Practicing leetcode problem #88 the topic being merge the two
# arrays by mutating them into the nums1 array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_pointer = len(nums1) - 1

        while n > 0 and m > 0:

            if nums1[m - 1] < nums2[n - 1]:
                nums1[nums1_pointer] = nums2[n - 1]
                n -= 1

            else:
                nums1[nums1_pointer] = nums1[m - 1]
                m -= 1

            nums1_pointer -= 1

        while n > 0:
            nums1[nums1_pointer] = nums2[n - 1]
            n -= 1
            nums1_pointer -= 1