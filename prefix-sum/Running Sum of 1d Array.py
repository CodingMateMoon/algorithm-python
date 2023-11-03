from typing import List
class Solution:
    """
    1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
    """
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        result[0] = nums[0]
        for i in range(1, len(nums)):
            result[i] = result[i - 1] + nums[i]
        return result



if __name__ == '__main__':
    print(Solution().runningSum([1, 2, 3, 4]))
    print(Solution().runningSum([1, 1, 1, 1, 1]))
