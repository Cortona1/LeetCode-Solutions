# Author: Anthony Corton
# Date: 8/17/2021
# Description: Practicing leetcode problem #14 the topic being find the longest
# common prefix between strings in a list


class Solution:
    def longestCommonPrefix(self, strs) -> str:

        if not strs:        # base case empty list
            return ""

        prefix_string = ""
        counter = 0
        sorted_array = sorted(strs, key=len)

        while counter < len(sorted_array[0]):  # shortest string is limit

            if counter == 0:
                string_prefix = sorted_array[0][0]

            for index in range(len(sorted_array)):

                if index == 0:                 # first string prefix sets base
                    next_prefix = sorted_array[index][counter]

                else:
                    string_prefix = sorted_array[index][counter]

                    if string_prefix != next_prefix:
                        return prefix_string

            prefix_string += string_prefix
            string_prefix = ""
            counter += 1

        return prefix_string

test = Solution()
print(test.longestCommonPrefix(["flower","flow","flight"]))


