# Author: Anthony Corton
# Date: 9/11/2021
# Description: Practicing leetcode problem #121 the topic being given an
# array prices where prices[i] is the price of a given stock on the ith day
# return the maximum profit you can achieve from this array, if no profit
# possible return 0


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i, value in enumerate(prices):
            if i == 0:
                min_price = value

            elif value < min_price:
                min_price = value

            elif value - min_price > profit:
                profit = value - min_price

        return profit