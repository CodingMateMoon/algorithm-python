from typing import List
class Solution:
    """
    k만큼 0->1 바꿔서 연속된 1이 가장 길게 나오는 경우 찾기
    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    0 <= k <= nums.length
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            print(nums[i])



if __name__ == '__main__':
    print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))