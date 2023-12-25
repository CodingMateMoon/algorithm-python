from typing import List


# https://leetcode.com/problems/find-pivot-index/description/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


def test_pivotIndex():
    solution = Solution()
    """
    (1) leftmost index = 3
    1 + 7 + 3 = 5 + 6 = 11
    (2) leftmost index = -1
    (3) leftmost index = 0
    0 = 1 - 1 = 0
    
    """
    assert solution.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert solution.pivotIndex([1, 2, 3]) == -1
    assert solution.pivotIndex([2, 1, -1]) == 0
