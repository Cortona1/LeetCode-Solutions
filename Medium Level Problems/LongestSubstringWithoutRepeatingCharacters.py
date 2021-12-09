# Author: Anthony Corton
# Date: 12/9/2021
# Description: Practicing leetcode problem #3, from
# algorithim topic/Medium List, given a string s, find the longest
# substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length_substring = 0
        substring_set = set()
        len_substring_set = 0

        for i in range(len(s)):
            substring_set.add(s[i])
            len_substring_set += 1

            if len(substring_set) != len_substring_set:  # duplicate recorded
                substring_set = set()            # reset string and add new char
                substring_set.add(s[i])
                len_substring_set = 1

                back_track_index = 1

                # make sure to add all previous chars till duplicate
                while s[i - back_track_index] != s[i]:
                    substring_set.add(s[i - back_track_index])
                    len_substring_set += 1
                    back_track_index += 1

            else:
                if len_substring_set > max_length_substring:
                    max_length_substring = len_substring_set

        return max_length_substring
