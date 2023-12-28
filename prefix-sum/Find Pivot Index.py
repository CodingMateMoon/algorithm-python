from typing import List


# https://leetcode.com/problems/find-pivot-index/description/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums):
            if left_sum == (S - left_sum - x):
                return i
            left_sum += x
        return -1
    def pivotIndex_1(self, nums: List[int]) -> int:
        pivot_index = left_sum = right_sum = 0
        for num in nums:
            right_sum += num
        right_sum -= nums[0]
        for i in range(len(nums) - 1):
            print(f"[pivot : {i}] left : {left_sum} / right : {right_sum}")
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
            right_sum -= nums[i + 1]
            pivot_index += 1
        if left_sum == right_sum:
            return pivot_index
        return -1


def test_pivotIndex():
    solution = Solution()
    """
    (1) leftmost index = 3
    1 + 7 + 3 = 5 + 6 = 11
    (2) leftmost index = -1
    (3) leftmost index = 0
    0 = 1 - 1 = 0
    (4) expected : 5, actual 4
    -1, -1  
    """
    assert solution.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert solution.pivotIndex([1, 2, 3]) == -1
    assert solution.pivotIndex([2, 1, -1]) == 0
    assert solution.pivotIndex([-1, -1, 0, 1, 1, 0]) == 5
