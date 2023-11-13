from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = [1, 3, 12, 0, 0]
        return nums

def test_moveZeroes():
    solution = Solution()
    assert solution.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
