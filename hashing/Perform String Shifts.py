class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        return "cab"

def test_stringShift():
    solution = Solution()
    assert solution.stringShift("abc", [[0, 1], [1,2]]) == "cab"