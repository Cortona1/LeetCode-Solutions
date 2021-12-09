# Author: Anthony Corton
# Date: 9/07/2021
# Description: Practicing leetcode problem #111 the topic being given a binary
# tree return its minimum depth


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:

        # edge cases

        if root is None:
            return 0

        test_l = self.nodeSearch(root.left, 1)

        test_r = self.nodeSearch(root.right, 1)

        if test_l == 1 and test_r != 1:  # edge cases for if one side branch is null
            return test_r
        elif test_r == 1 and test_l != 1:
            return test_l

        return min(test_l, test_r)

    def nodeSearch(self, root, counter):

        if root is None:
            return counter

        counter += 1         # if node is not none we increment counter

        if root.left is None and root.right is None:
            return counter

        if root.left is None:
            return self.nodeSearch(root.right, counter)

        if root.right is None:
            return self.nodeSearch(root.left, counter)

        return min(self.nodeSearch(root.left, counter),
                   self.nodeSearch(root.right, counter))