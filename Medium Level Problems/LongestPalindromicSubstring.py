# Author: Anthony Corton
# Date: 12/9/2021
# Description: Practicing leetcode problem #5, from
# algorithim topic/Medium List, given a string s, find the longest
# palinndrome substring without repeating characters
# sources: https://www.youtube.com/watch?v=XYQecbcd6_c

class Solution:
    def longestPalindrome(self, s: str) -> str:
        string_count = 0
        palindrome_string = ""

        for i in range(len(s)):
            left_side = i
            right_side = i

            while left_side > -1 and right_side < len(s) and (
                    s[left_side] == s[right_side]):
                intermediate_length = right_side - left_side + 1
                if (intermediate_length > string_count):
                    string_count = intermediate_length
                    palindrome_string = s[left_side:right_side + 1]

                right_side += 1
                left_side -= 1

            left_side = i
            right_side = i + 1

            while left_side > -1 and right_side < len(s) and (
                    s[left_side] == s[right_side]):
                intermediate_length = right_side - left_side + 1
                if (intermediate_length > string_count):
                    string_count = intermediate_length
                    palindrome_string = s[left_side:right_side + 1]

                right_side += 1
                left_side -= 1

        return palindrome_string