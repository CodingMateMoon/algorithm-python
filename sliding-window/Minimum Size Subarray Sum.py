# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    """
    부분 집합의 합 중 target보다 크거나 같은 최소 길이의 부분 집합을 구합니다
    앞에서 부분 집합의 합 중 target이상인 값이 나와도 더 길이가 작은 부분 집합이 뒤에 있을 수 있습니다 ex) 2 + 3 + 1 + 2 < 4 + 3
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        sum = left = length = 0

        for i in range (len(nums)):
            if sum < target:
                sum += nums[i]
                length += 1
                continue
            sum -= nums[left]
            left += 1
            sum += nums[i]




        return 2
def test_minSubArrayLen():
    solution = Solution()
    # 4 + 3 = 7, length 2
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    # 4, length 1
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1
