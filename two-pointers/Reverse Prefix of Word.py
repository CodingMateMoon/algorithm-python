class Solution:
    # https://leetcode.com/problems/reverse-prefix-of-word/
    def reversePrefix(self, word: str, ch: str) -> str:

        for i in range (len(word)):
            if word[i] == ch:
                for j in (i, 0, -1):
                    print(f"[{j}]")

        return "dcbaefd"
def test_reversePrefix():
    solution = Solution()
    assert solution.reversePrefix("abcdefd", "d") == "dcbaefd"
    assert solution.reversePrefix("abcd", "z") == "abcd"
