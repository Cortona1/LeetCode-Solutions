# Author: Anthony Corton
# Date: 8/11/2021
# Description: Practicing leetcode problem #9 the topic being palindrome numbers

class Solution:
    def isPalindrome(self, x: int) -> bool:

        integer_string = str(x)
        string_length = len(str(x))
        first_half = ""
        second_half= ""
        counter = 0

        if string_length % 2 == 0:

            while counter < string_length / 2:
                first_half += integer_string[counter]
                second_half += integer_string[string_length -1 -counter]
                counter+=1

        else:
            while counter < (string_length / 2) - 1:
                first_half += integer_string[counter]
                second_half += integer_string[string_length - 1 - counter]
                counter += 1

        if first_half == second_half:
            return True
        return False



test = Solution()
print(test.isPalindrome(121))

