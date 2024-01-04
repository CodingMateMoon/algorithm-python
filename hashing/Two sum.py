from typing import List


# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = nums[0]
        for i in range (1, len(nums)):
            sum += nums[i]
            if sum == target:
                return [i - 1, i]
            sum -= nums[i - 1]
        return -1




def test_twoSum():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    assert solution.twoSum([3, 2, 3], 6) == [0, 2]
