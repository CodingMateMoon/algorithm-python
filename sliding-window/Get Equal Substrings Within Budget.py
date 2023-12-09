class Solution:
    # https://leetcode.com/problems/get-equal-substrings-within-budget/description/
    """
    1 <= s.length <= 105
    t.length == s.length
    0 <= maxCost <= 106
    s and t consist of only lowercase English letters.
    """
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
def test_equalSubstring():
    solution = Solution()
    assert solution.equalSubstring("abcd", "bcdf", 3)