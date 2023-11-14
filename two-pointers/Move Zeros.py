from typing import List


class Solution:
    """
    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
    0을 제외한 나머지 숫자에 대해 리스트를 만들고 0의 개수를 센 뒤에 뒤에 덧붙입니다
    """
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        return nums

def test_moveZeroes():
    solution = Solution()
    assert solution.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert solution.moveZeroes([0]) == [0]
