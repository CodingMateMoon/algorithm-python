from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

def test_rotate():
    solution = Solution()
    assert solution.rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]
