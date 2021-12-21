# Author: Anthony Corton
# Date: 12/20/2021
# Description: Practicing leetcode problem #11, from
# algorithim topic/Medium List, given an integer array
# find the container with the most water (biggest possible area)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_bound = 0
        right_bound = len(height) - 1
        max_area = 0

        while left_bound != right_bound:
            current_area = self.calculateArea(left_bound, right_bound, height)

            if current_area > max_area:
                max_area = current_area

            if height[left_bound] < height[right_bound]:
                left_bound += 1
            else:
                right_bound -= 1

        return max_area

    def calculateArea(self, left, right, height):
        # calculate area between pillars
        # first find shortest length

        if height[left] > height[right]:
            length = height[right]
        else:
            length = height[left]

        # calculate width

        width = right - left

        # print("the left side is", left)
        # print("the right side is", right)

        return length * width