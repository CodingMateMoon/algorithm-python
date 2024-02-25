from typing import List

#https://leetcode.com/problems/rotate-array/editorial/

class Solution:

    def rotate(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1
        return nums
    def rotate_3(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a
        return nums

    def rotate_2(self, nums: List[int], k: int) -> List[int]:
        # speed up the rotation
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]
        return nums

    def rotate_1(self, nums: List[int], k: int) -> List[int]:

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
