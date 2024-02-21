from typing import List

#https://leetcode.com/problems/rotate-array/editorial/

class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:

        length = len(nums)
        k = k % length

        for x in range(k):
            # shift 연산
            last_char = nums[length - 1]
            for i in range(length - 1, -1, -1):
                nums[i] = nums[i - 1]
            nums[0] = last_char

        return nums


def test_rotate():
    """
    k만큼 오른쪽으로 이동

    """
    solution = Solution()
    assert solution.rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]
