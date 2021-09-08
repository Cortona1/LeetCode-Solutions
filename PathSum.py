# Author: Anthony Corton
# Date: 9/08/2021
# Description: Practicing leetcode problem #112 the topic being given a binary
# tree return True or False depending on if the tree has a root-to-leaf path
# such that adding up all the values along the path equals targetSum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False

        test_l = self.helperTarget(root.left, root.val)

        test_r = self.helperTarget(root.right, root.val)

        if test_l == [] and test_r == []:      # edge for root only
            return (targetSum == root.val)

        return (targetSum in test_l or targetSum in test_r)

    def helperTarget(self, root, counter):

        if root is None:
            return []

        counter += root.val

        if root.left is None and root.right is None:
            return [counter]

        if root.left is not None and root.right is None:
            return self.helperTarget(root.left, counter)

        if root.right is not None and root.left is None:
            return self.helperTarget(root.right, counter)

        return self.helperTarget(root.left, counter) + self.helperTarget(
            root.right, counter)