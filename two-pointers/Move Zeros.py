from typing import List


class Solution:
    """
    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
    0을 제외한 나머지 숫자에 대해 리스트를 만들고 0의 개수를 센 뒤에 뒤에 덧붙입니다
    0이 나온 경우 right(length - 1)에 추가
    """
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        end = right = len(nums) - 1
        for i in range (0, len(nums)):
            if nums[i] == 0:
                if right <= i:
                    continue
                for j in range(i + 1, len(nums)):
                    nums[i] = nums[j]
                nums[end] = 0
                right -= 1




        return nums

"""
1,
"""
def test_moveZeroes():
    solution = Solution()
    assert solution.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert solution.moveZeroes([0]) == [0]
