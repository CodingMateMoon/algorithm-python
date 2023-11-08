class Solution:
    """
    1 <= s.length <= 100
    s consists of characters with ASCII values in the range [33, 122].
    s does not contain '\"' or '\\'.
    """
    def reverseOnlyLetters(self, s: str) -> str:

        start_index = 0
        string_list = []
        for i in range  (len(s)):
            if not s[i].isalpha():
                for j in range(i - 1, start_index, -1):
                    string_list.append(s[j])
                string_list.append(s[i])
                start_index = i + 1
            elif i == len(s) - 1:
                for j in range(i, start_index - 1, -1):
                    string_list.append(s[j])
        result = ''.join(string_list)
        return result



def test_reverseWords():
    solution = Solution()
    assert solution.reverseOnlyLetters("ab-cd") == "dc-ba"
    assert solution.reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    assert solution.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
