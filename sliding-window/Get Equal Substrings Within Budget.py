class Solution:
    # https://leetcode.com/problems/get-equal-substrings-within-budget/description/
    """
    1 <= s.length <= 105
    t.length == s.length
    0 <= maxCost <= 106
    s and t consist of only lowercase English letters.
    """
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        print(f"test : {ord('b') - ord('a')}")
        left = sum = 0

        for i in range(len(s)):


def test_equalSubstring():
    solution = Solution()
    """
    a + 1 = b
    b + 1 = c
    c + 1 = d
    => max_length of a substring = 3
    
    a + 2 = c
    b + 2 = d
    maxCost = 3
    => max_length of a substring = 1
    """
    assert solution.equalSubstring("abcd", "bcdf", 3) == 3
    assert solution.equalSubstring("abcd", "cdef", 3) == 1
    assert solution.equalSubstring("abcd", "acde", 0) == 1
