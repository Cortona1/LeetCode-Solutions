# Author: Anthony Corton
# Date: 8/18/2021
# Description: Practicing leetcode problem #26 the topic being remove duplicates
# from an array without making another array while keeping relative order


class Solution:
    def removeDuplicates(self, nums):
        counter = 0

        while counter < len(nums):
            if counter == 0:
                previous_number = nums[counter]

            elif nums[counter] == previous_number:
                del nums[counter]
                counter -= 1  # counter must be shortened since list length is

            elif nums[counter] != previous_number:
                previous_number = nums[counter]

            counter += 1


"""
Second 'Pythonic' solution

for number in nums:
    while nums.count(number) > 1:
        nums.remove(number)

"""

test = Solution()
test_list = [0,0,1,1,1,2,2,3,3,4,4,4,5,6,6,7,7,8]
(test.removeDuplicates(test_list))
print(test_list)
