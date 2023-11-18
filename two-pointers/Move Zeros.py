from typing import List


class Solution:
    """
    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
    0을 제외한 나머지 숫자에 대해 리스트를 만들고 0의 개수를 센 뒤에 뒤에 덧붙입니다
    0이 나온 경우 right(length - 1)에 추가
    """
    def moveZeroes(self, nums: List[int]) -> List[int]:
        zero_count = 0

        for num in nums:
            zero_count += (num == 0)
        answer = []

        for num in nums:
            if num != 0:
                print(f"num : {num}")
                answer.append(num)

        for num in answer:
            print(num)

        for i in range(zero_count):
            answer.append(0)

        return nums

    def moveZeroes_1(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_count] = nums[i]
                non_zero_count += 1
        for i in range(non_zero_count, len(nums)):
            nums[i] = 0
        return nums

"""
1,
"""
def test_moveZeroes():
    solution = Solution()
    assert solution.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert solution.moveZeroes([0]) == [0]
