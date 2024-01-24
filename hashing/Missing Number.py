from typing import List

# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4602/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        is_exist = [False] * (len(nums) + 1)

        for i in range(len(nums)):
            is_exist[nums[i]] = True

        for i in range(len(is_exist)):
            if not is_exist[i]:
                return i
        return 0

def test_missingNumber():
    """
    [0, n] 중 빠진 숫자
    """
    solution = Solution()
    assert solution.missingNumber([3,0,1]) == 2
    assert solution.missingNumber([0, 1]) == 2
    assert solution.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
