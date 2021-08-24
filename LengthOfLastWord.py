# Author: Anthony Corton
# Date: 8/24/2021
# Description: Practicing leetcode problem #58 the topic find the length of
# the last word in a string (exclude spaces)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0                       # count holds intermediate values
        max_count = 0                   # max count hold final tally of word
        for number in range(len(s)):
            if s[number] == " ":
                if count != 0:          # assign count to max only if not 0
                    max_count = count   # to prevent against false resets

                count = 0

            else:
                count += 1

        if count != 0:                  # edge case for words not ending in " "
            max_count = count

        return max_count










test = Solution()
print(test.lengthOfLastWord("   fly me   to   the moon  "))
print(test.lengthOfLastWord("luffy is still joyboy"
))