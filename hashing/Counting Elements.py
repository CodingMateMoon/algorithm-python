from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:


def test_countElements():
    """
    x, x+1 연속된 숫자쌍이 있는 경우 구하기
    1 <= arr.length <= 1000
    0 <= arr[i] <= 1000
    """
    solution = Solution()
    assert solution.countElements([1, 2, 3]) == 2
    assert solution.countElements([1, 1, 3, 3, 5, 5, 7, 7]) == 0
