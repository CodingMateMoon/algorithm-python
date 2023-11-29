# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    """
    부분 집합의 합 중 target보다 크거나 같은 최소 길이의 부분 집합을 구합니다
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        return 2
def test_minSubArrayLen():
    solution = Solution()
    # 4 + 3 = 7, length 2
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    # 4, length 1
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1
