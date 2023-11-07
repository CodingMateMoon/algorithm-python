class Solution:
    """
    1 <= s.length <= 100
    s consists of characters with ASCII values in the range [33, 122].
    s does not contain '\"' or '\\'.
    """
    def reverseOnlyLetters(self, s: str) -> str:
def test_reverseWords():
    solution = Solution()
    assert solution.reverseOnlyLetters("ab-cd") == "dc-ba"
    assert solution.reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    assert solution.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
