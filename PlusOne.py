# Author: Anthony Corton
# Date: 8/24/2021
# Description: Practicing leetcode problem #66 the topic being given a non-empty
# array of decimal digits representing a non-negative integer, increment one
# to the integer.


class Solution:
    def plusOne(self, digits):
        if digits[len(digits) - 1] + 1 > 9:

            carry = 1
            digits[len(digits) - 1] = 0
            counter = len(digits) - 2

            while counter >= 0:               # work backwards on digit
                if digits[counter] + carry > 9:
                    digits[counter] = 0
                    counter -= 1

                else:
                    digits[counter] += 1
                    break

            if digits[0] == 0:               # edge case for increasing digit
                digits.insert(0, 1)          # length on carry

        else:
            digits[len(digits) - 1] += 1

        return digits


test = Solution()
test_list = [0]
test.plusOne(test_list)
print(test_list)

test = Solution()
test_list = [9]
test.plusOne(test_list)
print(test_list)

test = Solution()
test_list = [2, 9, 9]
test.plusOne(test_list)
print(test_list)

test = Solution()
test_list = [2, 9, 8]
test.plusOne(test_list)
print(test_list)

test = Solution()
test_list = [9, 9]
test.plusOne(test_list)
print(test_list)