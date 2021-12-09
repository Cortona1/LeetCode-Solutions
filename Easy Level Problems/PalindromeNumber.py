# Author: Anthony Corton
# Date: 8/11/2021
# Description: Practicing leetcode problem #9 the topic being palindrome numbers

class Solution:
    def isPalindrome(self, x: int) -> bool:

        return (str(x) == str(x)[::-1])



