# https://leetcode.com/problems/minimum-size-subarray-sum/
import sys
from typing import List


class Solution:
    """
    부분 집합의 합 중 target보다 크거나 같은 최소 길이의 부분 집합을 구합니다
    앞에서 부분 집합의 합 중 target이상인 값이 나와도 더 길이가 작은 부분 집합이 뒤에 있을 수 있습니다 ex) 2 + 3 + 1 + 2 < 4 + 3
    리스트 내림차순 정렬 후 가장 큰 값부터 하나씩 더해서 target 이상의 값을 가지는 최소 길이의 부분 집합의 합을 구합니다
    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = sys.maxsize

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = 0
                for k in range(i, j + 1):
                    sum += nums[k]
                if sum >= target:
                    min_length = min(min_length, j - i + 1)
                    break

        if min_length != sys.maxsize:
            return min_length
        return 0

    def minSubArrayLen_2(self, target: int, nums: List[int]) -> int:
        sum = left = 0
        min_length = sys.maxsize

        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                min_length = min(min_length, i + 1 - left)
                sum -= nums[left]
                left += 1

        if min_length != sys.maxsize:
            return min_length
        return 0
        # return min_length if min_length != sys.maxsize else 0

    def minSubArrayLen_1(self, target: int, nums: List[int]) -> int:

        sum = left = length = 0
        # sorted_list = sorted(nums, reverse=True)
        nums.sort(reverse=True)

        for i in range(len(nums)):
            if sum < target:
                sum += nums[i]
                length += 1
                continue
            elif target <= sum:
                return length

        if sum < target:
            return 0
        else:
            return length


def test_minSubArrayLen():
    solution = Solution()
    # 4 + 3 = 7, length 2
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    # 4, length 1
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1
    assert solution.minSubArrayLen(213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]) == 8
