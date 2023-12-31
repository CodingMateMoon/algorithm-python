class Solution(object):

    """
    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104
    """

    def findMaxAverage(self, nums, k):
        sum = 0.0
        for i in range (k):
            sum += nums[i]

        result = sum
        for i in range (k, len(nums)):
            sum += nums[i] - nums[i - k]
            result = max(result, sum)

        return result / k

    def findMaxAverage_2(self, nums, k):

        # Cumulative Sum
        sum = [0] * len(nums)
        sum[0] = nums[0]
        print(f"{nums[0]} : {sum[0]}")

        for i in range(1, len(nums)):
            sum[i] = sum[i - 1] + nums[i]
        result = sum[k - 1] * 1.0 / k
        print(f"result : {result}")

        for i in range(k, len(nums)):
            result = max(result, (sum[i] - sum[i - k]) * 1.0 / k)

        return result

    def findMaxAverage_1(self, nums, k):

        # right 커서를 1씩 증가시키면서 sum += num[right], length가 k를 넘을 경우 left + 1, sum -= num[left] 수행. max(answer, sum)
        # sum / length -> 평균 구하기
        left = length = 0
        answer = nums[0]
        sum = 0.0
        for right in range(len(nums)):
            sum += nums[right]
            length += 1
            if length > k:
                sum -= nums[left]
                left += 1
                length -= 1
            if right < k:
                answer = sum / k
                continue
            answer = max(answer, sum / k)

        return answer




        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

if __name__ == '__main__':
    # [ 12.75000 ] (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
    print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
    print(Solution().findMaxAverage([5], 1))
    print(Solution().findMaxAverage([-1], 1))
    print(Solution().findMaxAverage([4,0,4,3,3], 5))
    print(Solution().findMaxAverage([0,4,0,3,2], 1)) # 4.0


