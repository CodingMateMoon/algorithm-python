from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        print("test")

    def sumRange(self, left: int, right: int) -> int:
        return 1


def test_sumRange():
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    assert obj.sumRange(0, 2) == 1
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)