from typing import List
class Solution:

    """
    1 <= nums.length <= 100
    -100 <= nums[i] <= 100
    Input: nums = [-3,2,-3,4,2]
    Output: 5
    Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
    step by step sum
    startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
  left ~ right 합이 최소인 경우를 구하고 1보다 작을 경우 1이 되도록 만드는 값 x를 더해서 startValue를 구합니다.
    """
    def minStartValue(self, nums: List[int]) -> int:
        sum = nums[0]
        min_value = sum
        result = 1
        for i in range (1, len(nums)):
            sum += nums[i]
            min_value = min(sum,min_value)
        if (1 - min_value) < 1:
            return result
        return 1 - min_value





if __name__ == '__main__':
    print(Solution().minStartValue([-3, 2, -3, 4 , 2])) # 5