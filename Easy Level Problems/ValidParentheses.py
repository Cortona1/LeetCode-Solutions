# Author: Anthony Corton
# Date: 8/17/2021
# Description: Practicing leetcode problem #20 the topic being validate that
# parentheses and brackets have been properly closed.

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []            # use a stack to keep track of last inner symbol

        char_dictionary = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char not in char_dictionary:
                if len(stack) != 0:

                    inner_parentheses = stack.pop()

                    if char_dictionary[inner_parentheses] != char:
                        return False
                else:
                    return False
            else:
                stack.append(char)

        if len(stack) > 0:
            return False

        return True


test = Solution()
print(test.isValid("]"))