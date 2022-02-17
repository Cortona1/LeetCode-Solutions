# Author: Anthony Corton
# Date: 02/17/2022
# Description: Practicing leetcode problem #557 Reverse Words in a String III
# given a string s reverse the order of the characters in each word within
# a sentence. Solved in O(ab) time complexity.

class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ""
        word_array = s.split()

        for count, word in enumerate(word_array):

            for i in range(len(word) - 1, -1, -1):
                answer += word[i]

            if count != len(word_array) - 1:
                answer += " "

        return answer