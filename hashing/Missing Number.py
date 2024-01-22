from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return 2

def test_missingNumber():
    solution = Solution()
    assert solution.missingNumber([3,0,1]) == 2