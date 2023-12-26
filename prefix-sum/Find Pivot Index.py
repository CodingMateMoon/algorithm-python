from typing import List


# https://leetcode.com/problems/find-pivot-index/description/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot_index = left_sum = right_sum = 0
        for pivot_index in range(len(nums)):
            for left in range(0, pivot_index):
                left_sum += nums[left]
            for right in range(pivot_index + 1, len(nums)):
                right_sum += nums[right]
            if left_sum == right_sum:
                return pivot_index
            left_sum = right_sum = 0

        return -1






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
