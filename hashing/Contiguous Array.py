from typing import List

# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4845/
class Solution:
    def findMaxLength_1(self, nums: List[int]) -> int:
        maxlen = 0
        for start in range(len(nums)):
            zeroes = 0
            ones = 0
            for end in range(start, len(nums)):
                if nums[end] == 0:
                    zeroes += 1
                else:
                    ones += 1
                if zeroes == ones:
                    maxlen = max(maxlen, end - start + 1)
        return maxlen
    def findMaxLength(self, nums: List[int]) -> int:
        arr = [-2] * (len(nums) * 2 + 1)
        arr[len(nums)] = -1
        maxlen, count = 0, 0
        for i in range(len(nums)):
            count += -1 if nums[i] == 0 else 1
            if arr[count + len(nums)] >= -1:
                maxlen = max(maxlen, i - arr[count + len(nums)])
            else:
                arr[count + len(nums)] = i
        return maxlen



def test_findMaxLength():
    solution = Solution()
    """
    Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
    """
    assert solution.findMaxLength([0, 1]) == 2
    assert solution.findMaxLength([0, 1, 0]) == 2

    # 0 1 1 0
    assert solution.findMaxLength([0,1,1,0,1,1,1,0]) == 4

