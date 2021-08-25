# Author: Anthony Corton
# Date: 8/25/2021
# Description: Practicing leetcode problem #67 the topic being given two binary
# strings a and b return their sum as a binary string

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        length_a = len(a) - 1
        length_b = len(b) - 1
        sum_string = ""
        carry = 0

        while length_a >= 0 or length_b >= 0:

            if length_a >= 0:
                value_a = a[length_a]

            if length_b >= 0:
                value_b = b[length_b]

            if (value_a == "1" and value_b == "1") or (
                    (value_a == "1" or value_b == "1") and carry == 1):

                if value_a == "1" and value_b == "1" and carry == 1:
                    sum_string = "1" + sum_string

                else:
                    sum_string = "0" + sum_string

                carry = 1

            elif value_a == "1" or value_b == "1" or carry == 1:

                sum_string = "1" + sum_string
                carry = 0

            else:
                sum_string = "0" + sum_string

            value_a = 0
            value_b = 0
            length_a -= 1
            length_b -= 1

        if carry:
            sum_string = "1" + sum_string

        return sum_string