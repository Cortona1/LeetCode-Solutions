# Author: Anthony Corton
# Date: 8/30/2021
# Description: Practicing leetcode problem #108 the topic being given a sorted
# array convert that into a height-balanced binary search tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums != []:
            mid_index = len(nums) // 2

            return TreeNode(nums[mid_index],
                            self.sortedArrayToBST(nums[:mid_index]),
                            self.sortedArrayToBST(nums[mid_index + 1:]))
