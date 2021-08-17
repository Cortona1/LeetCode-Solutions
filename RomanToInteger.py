# Author: Anthony Corton
# Date: 8/17/2021
# Description: Practicing leetcode problem #13 the topic being convert
# Roman numerals to integers


class Solution:
    def romanToInt(self, s: str) -> int:

        edge_cases = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400,
                      "CM": 900}

        if s in edge_cases:
            return edge_cases[s]

        normal_cases = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                        "M": 1000}

        counter = 0
        sum = 0
        while counter < len(s):

            if counter > 0 and s[counter - 1] + s[counter] in edge_cases:
                sum -= normal_cases[s[counter - 1]]
                sum += edge_cases[s[counter - 1] + s[counter]]

            else:
                sum += normal_cases[s[counter]]

            counter += 1

        return sum