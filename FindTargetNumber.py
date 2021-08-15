# Author: Anthony Corton
# Date: 8/14/2021
# Description: Practicing interview problem of getting 2 arrays and finding
# the largest number closest to the target number (Assumes both arrays same
# length)



def find_target(number_array_1, number_array_2, target_number):
    """Takes two arrays full of integers and a target number as a parameter
    and returns the closes number to the target"""

    number_array_1.sort()
    number_array_2.sort()

    closest_pair = ()
    column_range = len(number_array_1) - 1
    row_range = 0
    close_target_number = number_array_1[column_range] + number_array_2[row_range]

    while row_range  >= 0 and row_range < len(number_array_2) and column_range >= 0 and column_range < len(number_array_2):

        if number_array_1[column_range] + number_array_2[row_range] == target_number:
            return (number_array_1[column_range], number_array_2[row_range])

        elif number_array_1[column_range] + number_array_2[row_range] > target_number:


            if abs(target_number - close_target_number) > abs(target_number - (number_array_1[column_range] + number_array_2[row_range])):
                close_target_number = number_array_1[column_range] + number_array_2[row_range]
                closest_pair = (number_array_1[column_range], number_array_2[row_range])
            column_range -=1

        elif number_array_1[column_range] + number_array_2[row_range] < target_number:
            if abs(target_number - close_target_number) > abs(target_number - (number_array_1[column_range] + number_array_2[row_range])):
                close_target_number = number_array_1[column_range] + number_array_2[row_range]
                closest_pair = (number_array_1[column_range], number_array_2[row_range])
            row_range += 1


    return closest_pair



print(find_target([-1, 3, 8, 2, 9, 5], [4, 1, 2, 10, 5, 20], 24))

print(find_target([7, 4, 1, 10], [4, 5, 8, 7], 13))
