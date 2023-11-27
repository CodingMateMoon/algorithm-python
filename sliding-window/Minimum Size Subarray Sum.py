# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        return 2
def test_minSubArrayLen():
    solution = Solution()
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1
