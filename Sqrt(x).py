# Author: Anthony Corton
# Date: 8/25/2021
# Description: Practicing leetcode problem #69 the topic being given a
# non-negative integer x, compute and return the square root of x
# NO BUILT IN EXPONENT FUNCTION OR OPERATOR ALLOWED (pow(x, 0.5) or x ** 0.5)


class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:    # edge case for square root of 0
            return 0

        if x == 1:
            return 1  # edge case for square root of 1

        for i in range(x // 2 + 1):

            if i * i > x:
                return i - 1

        return i