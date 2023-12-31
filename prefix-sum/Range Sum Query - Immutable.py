from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
           sum += self.nums[i]
        return sum


def test_sumRange():
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    assert obj.sumRange(0, 2) == 1
    assert obj.sumRange(2, 5) == -1
    assert obj.sumRange(0, 5) == -3
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)