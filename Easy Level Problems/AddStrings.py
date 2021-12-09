# Author: Anthony Corton
# Date: 8/10/2021
# Description: Practicing leetcode problem #415 add two integers represented
# as a string and return the sum as a string.


class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        """The ord function will be used to convert characters of 1-9 to numbers
        while subtracting 48 from the result will allow for a 1:1 conversion
        to add strings of integers"""

        num_1_length = len(num1) - 1
        num_2_length = len(num2) - 1
        carry = 0
        sum_string = ""

        while num_1_length >= 0 or num_2_length >= 0:
            character_1, character_2 = 0, 0

            if num_1_length >= 0:
                character_1 = ord(num1[num_1_length]) - 48
                num_1_length -= 1

            if num_2_length >= 0:
                character_2 = ord(num2[num_2_length]) - 48
                num_2_length -= 1

            # check for carry (10 or more) when adding the 2 numbers

            intermediate_sum = character_1 + character_2 + carry

            if intermediate_sum > 9:
                carry = 1
            else:
                carry = 0

            sum_string = str(intermediate_sum)[-1] + sum_string

        if carry:
            sum_string = "1" + sum_string

        return sum_string


# Test case for checking addition of 123 and 10 as strings respectively
test = Solution()

if test.addStrings("123", "10") == "133":
    print("The program successfully adds 123 and 10 as strings")