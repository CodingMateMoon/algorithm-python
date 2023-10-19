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

        # start_value보다 작은 값과 큰 값 사이의 middle 구하고 이를 만족시키는 최소값 return
        # 요소가 -100일 때 최대 100 + 1이 나와야 sum이 0보다 클 수 있습니다

        m = 100
        left = 1
        right = m * len(nums) + 1

        while left < right:
            middle = (left + right) // 2


    def minStartValue_3(self, nums: List[int]) -> int:

        startValue = 1
        while True:
            isValid = True
            total = startValue
            for num in nums:
                total += num
                if total < 1:
                    startValue += 1
                    isValid = False
                    break
            if isValid == True:
                return startValue




    def minStartValue_2(self, nums: List[int]) -> int:
        # We use "total" for current step-by-step total, "min_val" for minimum
        # step-by-step total among all sums. Since we always start with
        # startValue = 0, therefore the initial current step-by-step total is 0,
        # thus we set "total" and "min_val" be 0.
        min_val = 0
        total = 0

        # Iterate over the array and get the minimum step-by-step total.
        for num in nums:
            total += num
            min_val = min(min_val, total)

        # We have to change the minimum step-by-step total to 1,
        # by increasing the startValue from 0 to -min_val + 1,
        # which is just the minimum startValue we want.
        return -min_val + 1

    def minStartValue_1(self, nums: List[int]) -> int:
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
    print(Solution().minStartValue([1,2])) # 5