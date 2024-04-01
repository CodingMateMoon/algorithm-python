from typing import List


# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4662/


class Solution:
    def largestUniqueNumber_1(self, nums: List[int]) -> int:
        occur_counts = {}

        for num in nums:
            occur_count = occur_counts.get(num, 0) + 1
            occur_counts[num] = occur_count

        max_num = -1
        for num, occur_count in occur_counts.items():
            if occur_count == 1:
                max_num = max(num, max_num)

        return max_num

    def largestUniqueNumber_2(self, nums: List[int]) -> int:
        nums.sort()

        x = 0

        for i in range(len(nums) - 1, -1,  -1):
            print(f"(x : {x}) / i : {i - x} : (i - x :{nums[i - x]}), (i - 1 - x :{nums[i - 1 - x]})")
            print((i - x) == 0)
            print(nums[i - x] != nums[i - 1 - x])
            if (i - x) == 0 or nums[i - x] != nums[i - 1 - x]:
                print(f"return : {i - x}")
                index = i - x
                return nums[index]

            while (i - x)> 0 and nums[i - x] == nums[i-1 -x]:
                print(f"i / {i - x} :{nums[i - x]} : {nums[i-1 -x]}")
                x += 1
                print(f"<i> : {i - x}")

        return -1
    def largestUniqueNumber_3(self, nums: List[int]) -> int:
        nums.sort()

        index = len(nums) - 1
        while index > -1:

            print(f"index : {index} / nums[{index}] : {nums[index]}")
            if index == 0 or nums[index] != nums[index - 1]:
                return nums[index]
                #print(f"return index : {index} / {nums[index]} != {nums[index - 1]}")

            while index > 0 and nums[index] == nums[index - 1]:
                index -= 1

            index -= 1
        return -1

    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            







def test_largestUniqueNumber():
    """
    1번만 있는 숫자 중 가장 큰 수
    Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
    :return:
    1 <= nums.length <= 2000
    0 <= nums[i] <= 1000
    """
    solution = Solution()
    assert solution.largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]) == 8
    assert solution.largestUniqueNumber([9, 9, 8, 8]) == -1
