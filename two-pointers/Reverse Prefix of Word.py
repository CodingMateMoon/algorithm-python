class Solution:
    # https://leetcode.com/problems/reverse-prefix-of-word/
    def reversePrefix(self, word: str, ch: str) -> str:

        return "dcbaefd"
def test_reversePrefix():
    solution = Solution()
    assert solution.reversePrefix("abcdefd", "d") == "dcbaefd"