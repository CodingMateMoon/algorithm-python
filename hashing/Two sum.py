from typing import List


# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = nums[0]
        for i in range (1, len(nums)):
            sum += nums[i]
            if sum == target:
                return [i - 1, i]
            sum -= nums[i - 1]
        return -1




def test_twoSum():
    solution = Solution()
    """
    연속된 합뿐만 아니라 0, 2 등 순서 및 위치 상관없이 두 인덱스 조합으로 가능, 0 ~ i - 1까지 각 요소에 대해 다른 하나와 sum을 구했을 때 
    target이 나오는 경우 구하기
    """
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    assert solution.twoSum([3, 2, 3], 6) == [0, 2]
