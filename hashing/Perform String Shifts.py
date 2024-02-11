class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        shift [direction, amount]
        :type shift: List[List[int]]
        :rtype: str
        """
        return "cab"

def test_stringShift():
    solution = Solution()
    """
    direction> 0 : left, 1 : right
    amount> e.g) [0, 1]
    [0,1] means shift to left by 1. "abc" -> "bca"
    """
    assert solution.stringShift("abc", [[0, 1], [1,2]]) == "cab"