#https://leetcode.com/problems/perform-string-shifts/description/
class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        shift [direction, amount]
        :type shift: List[List[int]]
        :rtype: str
        """
        for direction, amount in shift:
            if direction == 0:
                    

        return "cab"

def test_stringShift():
    solution = Solution()
    """
    direction> 0 : left, 1 : right
    amount> e.g) [0, 1]
    [0,1] means shift to left by 1. "abc" -> "bca"
    [1,2] means shift to right by 2. "bca" -> "cab"
    """
    assert solution.stringShift("abc", [[0, 1], [1,2]]) == "cab"