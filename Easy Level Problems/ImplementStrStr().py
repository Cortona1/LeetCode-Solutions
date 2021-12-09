# Author: Anthony Corton
# Date: 8/19/2021
# Description: Practicing leetcode problem #28 the topic being implement the
# strStr() which returns the first index that a substring starts at in the
# parent string


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        elif len(needle) > len(haystack):
            return -1

        else:
            len_needle = len(needle)

            for i in range(len(haystack)):

                if haystack[i:len_needle] == needle:  # use slicing too look
                    return i
                else:
                    len_needle += 1     # need to upp needle index as we search

        return -1


test = Solution()
print(test.strStr("Hello", "ello"))
test = Solution()
print(test.strStr("Hello", "llo"))

test = Solution()
print(test.strStr("aaaaa", "bba"))
