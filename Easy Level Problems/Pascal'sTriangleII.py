# Author: Anthony Corton
# Date: 9/11/2021
# Description: Practicing leetcode problem #119 the topic being given a an
# integer rowIndex, return the rowIndex(nth) row (0-indexed) of
# Pascal's triangle as a list


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        result = []

        if rowIndex == 0:         # edge cases for first two rows
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        for i in range(rowIndex + 1):  # increment range because 0-indexed
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1, 1])
            else:
                count = 0
                intermediate_list = [1]
                previous_row = result[i - 1]
                first_pair = 0
                second_pair = 1
                while count <= len(previous_row) - 2:
                    intermediate_list.append(
                        previous_row[first_pair] + previous_row[second_pair])
                    count += 1
                    first_pair += 1
                    second_pair += 1
                intermediate_list.append(1)
                result.append(intermediate_list)

                if i == rowIndex:
                    return intermediate_list
