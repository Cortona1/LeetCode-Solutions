# Author: Anthony Corton
# Date: 8/10/2021
# Description: Practicing leetcode problem #771 the topic being strings
# counting the instances of jewels in stones




class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        counter = 0

        for char in stones:
            if char in jewels:
                counter += 1

        return counter