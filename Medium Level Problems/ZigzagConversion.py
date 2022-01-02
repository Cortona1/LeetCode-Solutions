# Author: Anthony Corton
# Date: 12/24/2021
# Description: Practicing leetcode problem #6, from
# algorithim topic/Medium List, given an a string
# convert it to a zig zag and then read the
# conversion line by line #source: https://youtu.be/Q2Tw6gcVEwc

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:  return s

        result = ""

        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                result += s[i]
                if (r > 0 and r < numRows - 1 and i + increment - 2 * r < len(
                        s)):  # if we are in middle row
                    result += s[i + increment - 2 * r]

        return result