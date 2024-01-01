from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        n = len(nums)
        self.sums = [0] * n
        self.sums[0] = nums[0]
        for i in range(1, n):
            self.sums[i] = self.sums[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left - 1]


    def sumRange_1(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
           sum += self.nums[i]
        return sum


def test_sumRange():
    """
    -2 0 3 -5 2 -1
    -2 -2 1 -4 -2 -3

    1 2 3 4 5
    1 3 6 10 15

    """
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    assert obj.sumRange(0, 2) == 1
    assert obj.sumRange(2, 5) == -1
    assert obj.sumRange(0, 5) == -3
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)