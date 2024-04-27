from typing import List

# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4845/
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero_count = one_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1

        return min(zero_count, one_count) * 2

def test_findMaxLength():
    solution = Solution()
    """
    Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
    """
    assert solution.findMaxLength([0, 1]) == 2
    assert solution.findMaxLength([0, 1, 0]) == 2
    assert solution.findMaxLength([0,1,1,0,1,1,1,0]) == 4

