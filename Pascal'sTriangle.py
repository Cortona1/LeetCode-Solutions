# Author: Anthony Corton
# Date: 9/08/2021
# Description: Practicing leetcode problem #118 the topic being given a an
# integer numRows, return the numRows of Pascal's triangle as a list


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = []

        for i in range(numRows):
            if i == 0:                # first two rows of pascal are hardcoded
                result.append([1])
            elif i == 1:              # to establish a logical pattern
                result.append([1, 1])
            else:
                count = 0
                intermediate_list = [1]
                previous_row = result[i - 1]
                while count < i - 1:
                    intermediate_list.append(
                        previous_row[len(previous_row) // 2 - 1] + previous_row[
                            len(previous_row) // 2])
                    count += 1
                intermediate_list.append(1)
                result.append(intermediate_list)

        return result