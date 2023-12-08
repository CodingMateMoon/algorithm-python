class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
def test_equalSubstring():
    solution = Solution()
    assert solution.equalSubstring("abcd", "bcdf", 3)