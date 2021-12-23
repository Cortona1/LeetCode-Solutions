# Author: Anthony Corton
# Date: 12/23/2021
# Description: Practicing leetcode problem #12, from
# algorithim topic/Medium List, given an integer
# convert it to roman numerals, solved using conditional
# spam


class Solution:
    def intToRoman(self, num: int) -> str:

        number = 0
        result = ""

        while number != num:
            difference = num - number

            if difference >= 1000:
                result += "M"
                number += 1000

            elif difference >= 900:
                number += 900
                result += "CM"

            elif difference >= 500:
                result += "D"
                number += 500

            elif difference >= 400:
                number += 400
                result += "CD"

            elif difference >= 100:
                result += "C"
                number += 100

            elif difference >= 90:
                result += "XC"
                number += 90

            elif difference >= 50:

                result += "L"
                number += 50

            elif difference >= 40:
                result += "XL"
                number += 40

            elif difference >= 10:
                result += "X"
                number += 10

            elif difference >= 9:
                result += "IX"
                number += 9

            elif difference >= 5:
                result += "V"
                number += 5

            elif difference >= 4:
                result += "IV"
                number += 4

            elif difference >= 1:
                result += "I"
                number += 1

        return result
