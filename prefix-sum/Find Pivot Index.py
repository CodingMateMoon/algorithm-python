from typing import List


# https://leetcode.com/problems/find-pivot-index/description/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


def test_pivotIndex():
    solution = Solution()
    assert solution.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert solution.pivotIndex([1, 2, 3]) == -1
    assert solution.pivotIndex([2, 1, -1]) == 0
