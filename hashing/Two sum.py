from typing import List

# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

def test_twoSum():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15]) == 9
    assert solution.twoSum([3, 2, 4]) == 6
    assert solution.twoSum([3, 3]) == 6
