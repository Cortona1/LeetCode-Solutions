class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum == target:
                return [l + 1, r + 1]

            elif sum > target:
                r -= 1

            else:
                l += 1
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(len(numbers)):
            if i == 0:
                dict[target - numbers[i]] = i

            else:
                if dict.get(numbers[i]) is None:
                    dict[target - numbers[i]] = i
                else:
                    return [dict[numbers[i]] + 1, i + 1]
    """