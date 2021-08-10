# Author: Anthony Corton
# Date: 8/10/2021
# Description: Practicing leetcode problem #1108 the topic being strings
# specifically defanging an ip address

class Solution:

    def defangIPaddr(self, address: str) -> str:

        defanged_string = ""

        for char in address:
            if char == ".":
                defanged_string += "[.]"
            else:
                defanged_string += char

        return defanged_string



test = Solution()
print(test.defangIPaddr("1.1.1.1"))

