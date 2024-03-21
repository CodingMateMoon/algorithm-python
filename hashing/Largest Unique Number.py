from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        return 8

def test_largestUniqueNumber():
    """
    Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
    :return:
    """
    solution = Solution()
    assert solution.largestUniqueNumber([5,7,3,9,4,9,8,3,1]) == 8
