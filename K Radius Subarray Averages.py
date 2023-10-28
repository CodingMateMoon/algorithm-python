import math
from typing import List


class Solution:

    """
    n == nums.length
    1 <= n <= 105
    0 <= nums[i], k <= 105

    Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Explanation:
    - avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
    - The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
      Using integer division, avg[3] = 37 / 7 = 5.
    - For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
    - For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
    - avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.

    i = 3 -> total = 0~6 sum
    i = 4 -> total = total - left[0] + right[7]
    i = k -> total = total - left[i - k - 1] + right[i + k]
        """

    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # When a single element is considered then its average will be the number itself only.
        if k == 0:
            return nums

        n = len(nums)
        averages = [-1] * n

        # Any index will not have 'k' elements in it's left and right.
        if 2 * k + 1 > n:
            return averages

        # Generate 'prefix' array for 'nums'.
        # 'prefix[i + 1]' will be sum of all elements of 'nums' from index '0' to 'i'.
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # We iterate only on those indices which have atleast 'k' elements in their left and right.
        # i.e. indices from 'k' to 'n - k'
        for i in range(k, n - k):
            leftBound, rightBound = i - k, i + k
            subArraySum = prefix[rightBound + 1] - prefix[leftBound]
            average = subArraySum // (2 * k + 1)
            averages[i] = average

        return averages

    def getAverages_1(self, nums: List[int], k: int) -> List[int]:

        length = len(nums)
        answer = [0] * length
        left = total = 0
        right = 2 * k
        sub_length = 2 * k + 1
        if sub_length <= length:
            for i in range(sub_length):
                total += nums[i]
        for i in range(length):
            # length 9 case : i = 6, 6 + 3 = 9일때 최대 인덱스 8보다 더 커서 조건에 벗어납니다
            if i < k or length <= (i + k):
                answer[i] = -1
                continue
            if i > k:
                right += 1
                total = total - nums[left] + nums[right]
                left += 1
            answer[i] = math.floor(total / sub_length)

        return answer

if __name__ == '__main__':
    print(Solution().getAverages([7,4,3,9,1,8,5,2,6], 3) )